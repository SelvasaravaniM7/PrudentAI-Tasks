from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def resize_image(image_file, height):
    image = Image.open(image_file)
    ratio = height / image.height
    width = int(image.width * ratio)
    resized_image = image.resize((width, height))
    temp_file = BytesIO()
    resized_image.save(temp_file, format=image.format)
    temp_file.seek(0)
    return ContentFile(temp_file.read(), name=image_file.name)
