import requests
from PIL import Image, ImageFilter
import io
import os


def apply_style(image_path, api_key):
    """Apply style transfer using the DeepAI API."""
    api_url = 'https://api.deepai.org/api/fast-style-transfer'

    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return None

    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        headers = {'api-key': api_key}
        response = requests.post(api_url, files={'image': image_data}, headers=headers)

        if response.status_code == 200:
            result_url = response.json().get('output_url')
            if result_url:
                response = requests.get(result_url)
                img = Image.open(io.BytesIO(response.content))
                img.show()
                return img
            else:
                print("Error: No output URL received from API.")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Error in style transformation: {e}")
    return None


def apply_pixel_art(image_path):
    """Apply a pixel art effect to the image."""
    try:
        image = Image.open(image_path)
        scale_factor = 10

        if image.width < scale_factor or image.height < scale_factor:
            print("Warning: Image is too small for effective pixelation.")
            return image

        image = image.resize((image.width // scale_factor, image.height // scale_factor), Image.NEAREST)
        image = image.resize((image.width * scale_factor, image.height * scale_factor), Image.NEAREST)
        image.show()
        return image
    except Exception as e:
        print(f"Error in Pixel Art transformation: {e}")
        return None


def apply_watercolor(image_path):
    """Apply a simple watercolor effect using PIL."""
    try:
        image = Image.open(image_path)
        image = image.filter(ImageFilter.GaussianBlur(radius=5))
        image.show()
        return image
    except Exception as e:
        print(f"Error in Watercolor transformation: {e}")
        return None


def convert_image_styles(image_path, api_key):
    """Apply multiple styles to an image."""
    print("Applying Ghibli style...")
    apply_style(image_path, api_key)

    print("Applying Pixel Art effect...")
    apply_pixel_art(image_path)

    print("Applying Watercolor effect...")
    apply_watercolor(image_path)


if __name__ == '__main__':
    image_path = 'your_image.jpg'  # Replace with actual image path
    api_key = 'your_actual_api_key_here'  # Replace with a valid API key

    if os.path.exists(image_path):
        convert_image_styles(image_path, api_key)
    else:
        print(f"Error: The file '{image_path}' does not exist.")
