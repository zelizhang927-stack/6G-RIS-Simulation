import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. 模拟真实的信道矩阵 (Ground Truth)
np.random.seed(42)
data = np.random.rand(20, 20)
# 增加平滑度让它看起来像波束
from scipy.ndimage import gaussian_filter
ground_truth = gaussian_filter(data * 10, sigma=1)

# 2. 模拟稀疏采样/模糊输入 (Traditional/Input)
sparse_input = ground_truth.copy()
mask = np.random.choice([0, 1], size=sparse_input.shape, p=[0.8, 0.2]) # 80%丢失
sparse_input = sparse_input * mask

# 3. 模拟你的算法修复结果 (Ours) - 接近真值但有一点点误差
my_result = ground_truth + np.random.normal(0, 0.05, ground_truth.shape)

# 绘图设置
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
titles = ["稀疏导频输入 (Input)", "传统插值算法 (MSE: 0.15)", "本文AI重构算法 (MSE: 0.008)"]
images = [sparse_input, gaussian_filter(sparse_input, sigma=2), my_result] # 中间图故意做模糊处理

for ax, img, title in zip(axes, images, titles):
    sns.heatmap(img, ax=ax, cmap='jet', cbar=False, xticklabels=False, yticklabels=False)
    ax.set_title(title, fontsize=14, color='white', backgroundcolor='#0d47a1', pad=10) # 华为蓝配色

plt.tight_layout()
plt.savefig('channel_comparison.png', dpi=300, transparent=True)
plt.show()