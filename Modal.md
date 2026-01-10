[How to deploy LTX-2 with an API compatible with the OpenAI SDK](https://www.reddit.com/r/StableDiffusion/comments/1q8tuyg/how_to_deploy_ltx2_with_an_api_compatible_with/)

```py
import modal

aquiles_image = (
    modal.Image.from_registry("nvidia/cuda:12.8.0-devel-ubuntu22.04", add_python="3.12")
    .apt_install("git", 
        "curl", 
        "build-essential", 
        "wget", 
        "libgl1", 
        "libglib2.0-0", 
        "ffmpeg",
        "libavcodec-dev",  
        "libavformat-dev",  
        "libavutil-dev",
        "libswscale-dev",
        "libavfilter-dev",
        "libavdevice-dev", )
    .entrypoint([])
    .run_commands(
        "python -m pip install --upgrade pip",
        "python -m pip install --upgrade setuptools wheel",
    )
    .uv_pip_install(
        "torch==2.8",
        "git+https://github.com/huggingface/diffusers.git",
        "transformers==4.57.3",
        "tokenizers==0.22.1",
        "https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.3.14/flash_attn-2.8.2+cu128torch2.8-cp312-cp312-linux_x86_64.whl",
        "git+https://github.com/Aquiles-ai/Aquiles-Image.git",
        "bitsandbytes==0.49.0",
        "accelerate==1.12.0",
        "git+https://github.com/Lightricks/LTX-2.git#subdirectory=packages/ltx-core",
        "git+https://github.com/Lightricks/LTX-2.git#subdirectory=packages/ltx-pipelines",
        "av==16.0.1"
    )
    .env({"HF_XET_HIGH_PERFORMANCE": "1",
        "PYTORCH_CUDA_ALLOC_CONF": "expandable_segments:True"})  
)

MODEL_NAME = "ltx-2"

hf_cache_vol = modal.Volume.from_name("huggingface-cache", create_if_missing=True)
aquiles_config_vol = modal.Volume.from_name("aquiles-cache", create_if_missing=True)
aquiles_video_vol = modal.Volume.from_name("aquiles-video-cache", create_if_missing=True)

app = modal.App("aquiles-image-server-ltx-2")
 
N_GPU = 1
MINUTES = 60
AQUILES_PORT = 5500

@app.function(
    image=aquiles_image,
    gpu=f"H100:{N_GPU}",
    secrets=[modal.Secret.from_name("huggingface-secret")],
    scaledown_window=30 * MINUTES, 
    timeout=30 * MINUTES,
    volumes={
        "/root/.cache/huggingface": hf_cache_vol,
        "/root/.local/share": aquiles_config_vol,
        "/root/.local/share": aquiles_video_vol,
    },
)
@modal.concurrent(max_inputs=5)
@modal.web_server(port=AQUILES_PORT, startup_timeout=20 * MINUTES)
def serve():
    import subprocess

    cmd = [
        "aquiles-image",
        "serve",
        "--host",
        "0.0.0.0",
        "--port",
        str(AQUILES_PORT),
        "--model",
        MODEL_NAME,
        "--api-key", "dummy-api-key",
    ]

    print(f"Starting Aquiles-Image with the model:{MODEL_NAME}")
    print(f"Command {' '.join(cmd)}")

    subprocess.Popen(" ".join(cmd), shell=True)
```
