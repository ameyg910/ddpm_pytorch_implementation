import os
import torchvision
from PIL import Image

# Configuration
target_dir = 'data/train/images'
dataset = torchvision.datasets.MNIST(root='./raw_data', train=True, download=True)

for i, (img, label) in enumerate(dataset):
    # Create directory for the label if it doesn't exist (e.g., data/train/images/5)
    label_dir = os.path.join(target_dir, str(label))
    os.makedirs(label_dir, exist_ok=True)
    
    # Save the image
    img.save(os.path.join(label_dir, f"{i}.png"))

print("Done! Data directory is ready.")