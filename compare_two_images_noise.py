import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import estimate_sigma

# === 1. DEFINE YOUR IMAGES ===
# Dictionary format configured for images A through D
image_files = {
    "Image A": "image_A.jpg",
    "Image B": "image_B.jpg",
    "Image C": "image_C.jpg",
    "Image D": "image_D.jpg"
}

# === 2. ESTIMATE NOISE FOR EACH IMAGE AND LOAD ===
processed_data = []

for label, path in image_files.items():
    img = cv2.imread(path)
    
    if img is None:
        print(f"Warning: Could not load {path}. Using blank placeholder.")
        img_rgb = np.zeros((300, 300, 3), dtype=np.uint8)
        avg_sigma = 0.0
    else:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        sigma_channels = estimate_sigma(img_rgb, channel_axis=-1)
        avg_sigma = float(np.mean(sigma_channels))
    
    processed_data.append({
        "label": label,
        "image": img_rgb,
        "sigma": avg_sigma
    })

# === 3. CREATE THE VISUAL GRID ===
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.ravel()

max_sigma = max([item["sigma"] for item in processed_data]) if processed_data else 1.0
if max_sigma == 0:
    max_sigma = 1.0

for i, data in enumerate(processed_data):
    axs[i].imshow(data["image"])
    axs[i].axis("off")
    
    ratio = data["sigma"] / max_sigma
    if ratio > 0.66:
        border_color = "crimson"
    elif ratio > 0.33:
        border_color = "goldenrod"
    else:
        border_color = "seagreen"
        
    title_string = f"{data['label']}\nNoise Level (Sigma): {data['sigma']:.4f}"
    axs[i].set_title(title_string, fontsize=12, fontweight="bold", color=border_color, pad=10)
    
    for spine in axs[i].spines.values():
        spine.set_visible(True)
        spine.set_color(border_color)
        spine.set_linewidth(3)

plt.tight_layout()
plt.savefig('noise_comparison.png', dpi=300, bbox_inches='tight')
print("Noise comparison saved to noise_comparison.png")
print("\nNoise levels (Sigma):")
for data in processed_data:
    print(f"{data['label']}: {data['sigma']:.4f}")
