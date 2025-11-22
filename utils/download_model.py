# import os
# from huggingface_hub import snapshot_download

# # 1. 定义模型 ID
# repo_id = "Qwen/Qwen3-VL-4B-Instruct"

# # 2. 定义你本地的保存路径
# # (确保 playground/Pretrained_models 存在)
# local_dir = os.path.join("playground", "Pretrained_models", repo_id.split('/')[-1])

# # 3. 确保目标文件夹存在
# os.makedirs(local_dir, exist_ok=True)

# print(f"正在下载模型 {repo_id} 到 {local_dir} ...")

# # 4. 执行下载
# snapshot_download(
#     repo_id=repo_id,
#     local_dir=local_dir,
#     ignore_patterns=["*.pt", "*.bin"], # 可选：只下载 .safetensors 格式，忽略旧格式
# )

# print(f"模型下载完成！")
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="StarVLA/Qwen3VL-GR00T-Bridge-RT-1",
    local_dir="./StarVLA/Qwen3VL-GR00T-Bridge-RT-1",
    allow_patterns=["config.yaml", "dataset_statistics.json", "checkpoints/*.pt"],
    local_dir_use_symlinks=False,
)