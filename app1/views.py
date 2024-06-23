from django.shortcuts import render
import os
from pathlib import Path
import PIL
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)   

def processimg(img,name):
    new_image_data = pixels_to_ascii(grayify(resize_image(img)))

    pixel_count = len(new_image_data)  
    ascii_image = "\n".join(new_image_data[i:(i+100)] for i in range(0, pixel_count, 100))

    return ascii_image


def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        img=request.FILES['img']

        asciiimg=processimg(img,name)
        

        return render(request,"home.html",{'asciiimg':asciiimg,'name':name})

        pass
    return render(request,"home.html")
