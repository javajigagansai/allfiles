import cv2
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
import AnimeGANv2  # Ensure you have the AnimeGANv2 model installed and trained

# Load the AnimeGANv2 model
model = AnimeGANv2.load_model("path_to_ghibli_model.pth")  # Replace with actual model path
model.eval()

def ghibli_style_transfer(image_path, output_path):
    """Converts an image to Ghibli style using AnimeGANv2"""
    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    input_tensor = transform(image).unsqueeze(0)

    # Apply the model
    with torch.no_grad():
        output_tensor = model(input_tensor)

    # Convert tensor back to image
    output_image = output_tensor.squeeze(0).detach().cpu().numpy()
    output_image = np.transpose(output_image, (1, 2, 0))
    output_image = ((output_image + 1) * 127.5).astype(np.uint8)
    output_image = cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR)

    # Save the high-quality image
    cv2.imwrite(output_path, output_image)
    print(f"Ghibli-style image saved at {output_path}")

# Example usage
ghibli_style_transfer("input.jpg", "output.jpg")
