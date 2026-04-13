import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the AnimeGANv2 model
model = load_model("path_to_ghibli_model.h5")  # Replace with actual model path

def ghibli_style_transfer(image_path, output_path):
    """Converts an image to Ghibli style using AnimeGANv2"""
    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    input_tensor = transform(image).unsqueeze(0).numpy()

    # Apply the model
    output_tensor = model.predict(input_tensor)

    # Convert tensor back to image
    output_image = output_tensor.squeeze(0)
    output_image = np.transpose(output_image, (1, 2, 0))
    output_image = ((output_image + 1) * 127.5).astype(np.uint8)
    output_image = Image.fromarray(output_image)

    # Save the high-quality image
    output_image.save(output_path)
    print(f"Ghibli-style image saved at {output_path}")

# Example usage
ghibli_style_transfer("input.jpg", "output.jpg")