from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image as PilImage
from io import BytesIO
from .models import Image

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Image

@csrf_exempt  
def upload_image(request):
    pass

def get_image_urls(request, id):
    pass


def index(request):
    return render(request, 'index.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        original_image = request.FILES['image']
        image_instance = Image.objects.create(original_image=original_image)

        img = PilImage.open(original_image)
        
        small_img = img.resize((int(img.width * 100 / img.height), 100))
        small_img_io = BytesIO()
        small_img.save(small_img_io, format='JPEG')
        small_img_io.seek(0)
        image_instance.small_image.save(f"small_{original_image.name}", small_img_io, save=False)
        
        medium_img = img.resize((int(img.width * 300 / img.height), 300))
        medium_img_io = BytesIO()
        medium_img.save(medium_img_io, format='JPEG')
        medium_img_io.seek(0)
        image_instance.medium_image.save(f"medium_{original_image.name}", medium_img_io, save=False)

        image_instance.save()

        return JsonResponse({'id': image_instance.id})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_image_urls(request, id):
    try:
        image_instance = Image.objects.get(id=id)
        data = {
            'original_image': image_instance.original_image.url,
            'small_image': image_instance.small_image.url,
            'medium_image': image_instance.medium_image.url
        }
        return JsonResponse(data)
    except Image.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)
