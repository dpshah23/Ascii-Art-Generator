# Image to ASCII Art Converter - Django Web App

## Overview
The Image to ASCII Art Converter is a Django-based web application that transforms images into ASCII art. Users can upload images through the web interface, and the application will convert them into visually appealing ASCII art, which can be viewed on the website or downloaded as a text file.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Customization](#customization)
6. [Example](#example)
7. [Contact](#contact)

## Features
- **Web Interface:** User-friendly web interface for uploading images and viewing ASCII art.
- **Image Conversion:** Converts various image formats (JPEG, PNG, BMP, etc.) to ASCII art.
- **Customizable Output:** Allows customization of the ASCII characters used for conversion.
- **File Output:** Option to download the generated ASCII art as a text file.
- **Responsive Design:** Mobile-friendly and responsive web design.

## Requirements
- Python 3.x
- Django 3.x or higher
- Pillow (Python Imaging Library)
- NumPy

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/dpshah23/Ascii-Art-Generator.git
    cd image-to-ascii-art-django
    ```
2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000` to access the app.

## Usage
1. Open the web application in your browser.
2. Upload an image using the provided upload form.
3. Click "Convert" to transform the image into ASCII art.
4. View the ASCII art directly on the web page.
5. Optionally, download the ASCII art as a text file.

## Customization
You can customize the ASCII characters used for conversion by editing the `ASCII_CHARS` variable in the `convert.py` script:
```python
ASCII_CHARS = "@%#*+=-:. "
```

## Example
### Home Page
![home_page](path_to_home_page_screenshot)

### ASCII Art Result
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
...
```

## Contact
For any inquiries, please contact [dpshah2307@gmail.com](mailto:dpshah2307@gmail.com).
