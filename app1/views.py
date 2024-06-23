from django.shortcuts import render
from pathlib import Path
from app1.models import Asciiart
from PIL import Image
import os
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from asciigenerator import settings



ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

BASE_DIR = Path(__file__).resolve().parent.parent

def resize_image(image, max_width=100, max_height=None):
    width, height = image.size
    
    aspect_ratio = width / float(height)
  
    if max_height is not None:
        max_width = min(max_width, aspect_ratio * max_height)
    else:
        max_height = max_width / aspect_ratio
    
    resized_image = image.resize((int(max_width), int(max_height)), Image.LANCZOS)
    
    return resized_image


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def process_image(img):
    resized_image = resize_image(img)
    grayscale_image = grayify(resized_image)
    ascii_data = pixels_to_ascii(grayscale_image)
    
    pixel_count = len(ascii_data)
    ascii_image = "\n".join(ascii_data[i:(i + 100)] for i in range(0, pixel_count, 100))
    
    return ascii_image

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        uploaded_image = request.FILES['image']
        # Define the file path for the saved image
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fs.url(filename)

        # Open and process the image
        uploaded_image_path = os.path.join(settings.MEDIA_ROOT, filename)
        with Image.open(uploaded_image_path) as img:
            img = img.convert("RGB")  # Ensure the image is in RGB format
            img = img.resize((100, 100), Image.LANCZOS)  # Resize if necessary

            # Save the image as a .jpg file
            jpg_image_path = os.path.splitext(uploaded_image_path)[0] + '.jpg'
            img.save(jpg_image_path, 'JPEG')

           
            ascii_art = process_image(img)

        context = {
            'uploaded_image_url': uploaded_image_url,
            'ascii_art': ascii_art
        }
        return render(request, 'home.html', context)

    return render(request, 'home.html')