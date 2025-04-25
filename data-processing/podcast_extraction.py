import yaml
from docetl.api import (
    Pipeline,
    Dataset,
    MapOp,
    ReduceOp,
    SplitOp,
    UnnestOp,
    ResolveOp,
    PipelineStep,
    PipelineOutput,
    GatherOp,
    ParallelMapOp,
)

# Define the pipeline
pipeline = Pipeline(
    name="podcast_analysis",
    datasets={
        "podcast_transcript": Dataset(
            type="file",
            path="data.json", # file with [{"transcript": "..."}]
        )
    },
    operations=[
        SplitOp(
            name="split_transcript",
            type="split",
            split_key="transcript",
            method="token_count",
            method_kwargs={"num_tokens": 2000},
        ),
        GatherOp(
            name="gather_transcripts",
            type="gather",
            content_key="transcript_chunk",
            doc_id_key="split_transcript_id",
            order_key="split_transcript_chunk_num",
            peripheral_chunks={
                "previous": {"tail": {"count": 0.25}}
            },  # Gets 25% of the previous chunk
        ),
        ParallelMapOp(
            name="extract_insights",
            type="parallel_map",
            prompts=[
                {
                    "prompt": """
                    Analyze the following chunk of a podcast transcript:

                    {{ input.transcript_chunk_rendered }}

                    Extract a list of insights related to frameworks. In this context, a framework could refer to a structured approach, methodology, or way of thinking about a particular topic or problem. It might be a conceptual model, a set of principles, or a systematic process discussed in the podcast. Provide detailed descriptions for each insight, explaining how the framework is presented or applied in the discussion.

                    Format your response as a list of strings.
                    """,
                    "output_keys": ["framework_insights"],
                },
                {
                    "prompt": """
                    Analyze the following chunk of a podcast transcript:

                    {{ input.transcript_chunk_rendered }}

                    Extract a list of insights related to technologies. For each technology mentioned:
                    
                    1. Identify the specific technology.
                    2. Briefly explain its application or relevance in the discussion.
                    3. Note any key benefits, challenges, or unique features mentioned.
                    4. If applicable, include any comparisons or future developments discussed.

                    Provide concise but informative descriptions for each technological insight.
                    """,
                    "output_keys": ["technology_insights"],
                },
                {
                    "prompt": """
                    Analyze the following chunk of a podcast transcript:

                    {{ input.transcript_chunk_rendered }}

                    Extract a list of insights related to products. A product here refers to any offering discussed in the podcast, such as software, services, platforms, or physical goods. For each product:
                    
                    1. Identify the product.
                    2. Briefly describe its purpose and key features.
                    3. Note any benefits, challenges, or comparisons mentioned.

                    Provide concise but informative descriptions for each product insight.

                    Format your response as a list of strings.
                    """,
                    "output_keys": ["product_insights"],
                },
                {
                    "prompt": """
                    Analyze the following chunk of a podcast transcript:

                    {{ input.transcript_chunk_rendered }}

                    Extract a list of insights related to stories shared in the podcast. Focus on what makes these stories compelling or relevant in the context of a podcast. For each story:

                    1. Identify the main narrative or anecdote.
                    2. Explain why it's interesting or impactful in the podcast format.
                    3. Note any lessons, morals, or key takeaways from the story.
                    4. If applicable, describe how the story relates to the podcast's overall theme or topic.

                    Consider elements that make stories effective in audio format, such as vivid descriptions, emotional resonance, or unique perspectives. Provide detailed descriptions for each insight, highlighting what makes these stories particularly engaging or memorable for podcast listeners.
                    """,
                    "output_keys": ["story_insights"],
                },
            ],
            output={
                "schema": {
                    "framework_insights": "list[str]",
                    "technology_insights": "list[str]",
                    "product_insights": "list[str]",
                    "story_insights": "list[str]",
                }
            },
        ),
        MapOp(
            name="transform_insights",
            type="map",
            prompt="""
            Given the following insights from a podcast transcript:

            Framework insights: {{ input.framework_insights }}
            Technology insights: {{ input.technology_insights }}
            Product insights: {{ input.product_insights }}
            Story insights: {{ input.story_insights }}

            Transform these into a list of insights, where each insight has a type, title, and description.
            The type should be one of: "framework", "technology", "product", or "story".
            The title should be a short, descriptive phrase for the insight (5 words).
            The description should provide more detail about the insight.

            Your answer should have the most salient ~5-10 insights.
            """,
            output={
                "schema": {
                    "insights": "list[{type: string, title: string, description: string}]"
                }
            },
        ),
        UnnestOp(
            name="flatten_insights",
            type="unnest",
            unnest_key="insights",
            recursive=True,
        ),
        ResolveOp(
            blocking_threshold=0.4141,
            name="canonicalize_insights",
            type="resolve",
            blocking_keys=["description", "title"],
            comparison_prompt="""
            Compare the following two insights from the podcast:
            Insight 1: {{ input1.title }}
            Insight 2: {{ input2.title }}
            Are these referring to the same or similar insight? Consider variations in naming, abbreviations, or contextual clues. 
            Respond with "True" if they are the same, or "False" if they are different.
            """,
            resolution_prompt="""
            Given the following similar insights from the podcast:
            {% for input in inputs %}
            - {{ input.title }}
            {% endfor %}
            Provide a single, canonical insight for this. Choose the most accurate, widely recognized, or official term.
            """,
            output={"schema": {"title": "string"}},
            embedding_model="text-embedding-3-small",
            comparison_model="gpt-4o-mini",
            resolution_model="gpt-4o-mini",
        ),
        ReduceOp(
            name="summarize_insights",
            type="reduce",
            reduce_key=["description", "split_transcript_id"],
            prompt="""
            Here's a podcast transcript:
            {{ inputs[0].transcript }}
            For the following insight: {{ inputs[0].title }} (a {{ inputs[0].type }} insight)
            with description: {{ inputs[0].description }}
            
            Provide a detailed expansion of the insight in a bullet point format.
            """,
            output={"schema": {"expanded_insight": "string"}},
            pass_through=True,
        ),
        MapOp(
            name="select_relevant_keys",
            type="map",
            drop_keys=[
                "transcript_chunk",
                "transcript_chunk_rendered",
                "transcript",
                "split_transcript_id",
                "split_transcript_chunk_num",
                "insights",
                "technology_insights",
                "framework_insights",
                "product_insights",
                "story_insights",
            ],
        ),
    ],
    steps=[
        PipelineStep(
            name="podcast_analysis",
            input="podcast_transcript",
            operations=[
                "split_transcript",
                "gather_transcripts",
                "extract_insights",
                "transform_insights",
                "flatten_insights",
                "canonicalize_insights",
                "summarize_insights",
                "select_relevant_keys",
            ],
        ),
    ],
    output=PipelineOutput(
        type="file",
        path="podcast_analysis.json",
        intermediate_dir="intermediate_podcasts",
    ),
    default_model="gpt-4o-mini",
)

# Optimize the pipeline
# I commented this out becaue i updated the resolve op to include the blocking threshold found (0.4141)
# # optimized_pipeline = pipeline.optimize()
# # config = optimized_pipeline._to_dict()

# with open(
#     "pipeline.yaml",
#     "w",
# ) as f:
#     yaml.dump(config, f)


# Run the pipeline
pipeline.run()
