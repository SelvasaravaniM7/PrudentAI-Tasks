from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name='index'), 
    path('api/v1/image/', views.upload_image, name='upload_image'),
    path('api/v1/image/<int:id>/', views.get_image_urls, name='get_image_urls'),
]
