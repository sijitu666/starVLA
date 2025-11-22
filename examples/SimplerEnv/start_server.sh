your_ckpt=/home/zhiwei/robotics/v2a/starVLA/StarVLA/Qwen3VL-GR00T-Bridge-RT-1/checkpoints/steps_20000_pytorch_model.pt
sim_python=/mnt/conda/zhiwei/miniconda3/envs/starVLA/bin/python
port=5678
# DEBUG=true


CUDA_VISIBLE_DEVICES=0 ${sim_python} deployment/model_server/server_policy.py \
    --ckpt_path ${your_ckpt} \
    --port ${port} \
    --use_bf16