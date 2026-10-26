[Evidence-Aware RAG Evaluation: Why Ground Truth Coverage Determines Retrieval Scores in Clinical Agent Systems](https://dev.to/mech_app_ai/evidence-aware-rag-evaluation-why-ground-truth-coverage-determines-retrieval-scores-in-clinical-5c6d)

## Retrieval Pipeline Architecture

```py
# Pseudocode illustrating three-stage retrieval pipeline
# Stage 1: Parallel sparse and dense retrieval
bm25_results = bm25_index.search(query, top_k=100)
dense_results = embedding_model.search(query, top_k=100)

# Stage 2: Merge and deduplicate
# merge_results() is a custom function that unions result sets
# and removes duplicate chunk IDs
candidate_pool = merge_results(bm25_results, dense_results)

# Stage 3: Cross-encoder reranking
reranked = cross_encoder.rerank(
    query=query,
    candidates=candidate_pool,
    top_k=5
)
```

