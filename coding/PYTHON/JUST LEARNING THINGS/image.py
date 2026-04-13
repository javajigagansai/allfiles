import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import requests
from io import BytesIO


def load_model(model_name):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_name).to(device)
    return pipe


def transform_image(image_path, prompt, model):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((512, 512))

    pipe = load_model(model)
    generator = torch.manual_seed(42)
    transformed_image = pipe(prompt=prompt, image=image, strength=0.75, guidance_scale=7.5, generator=generator).images[
        0]

    return transformed_image


def main():
    image_path = input("Enter image path: ")
    prompt = input("Enter a description of the transformation (e.g., 'Ghibli style', '3D render', 'Anime art'): ")

    style_models = {
        "ghibli": "nitrosocke/Ghibli-Diffusion",
        "anime": "hakurei/waifu-diffusion",
        "3d": "stabilityai/stable-diffusion-3d",
        "art": "CompVis/stable-diffusion-v1-4"
    }

    style = prompt.lower().strip()
    model = style_models.get(style, "CompVis/stable-diffusion-v1-4")

    print(f"Using model: {model}")
    transformed_image = transform_image(image_path, prompt, model)
    transformed_image.show()
    transformed_image.save("output.png")
    print("Saved transformed image as output.png")


if __name__ == "__main__":
    main()
