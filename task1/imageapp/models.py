from django.db import models

class Image(models.Model):
    original_image = models.ImageField(upload_to='originals/')
    small_image = models.ImageField(upload_to='small/', null=True, blank=True)
    medium_image = models.ImageField(upload_to='medium/', null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"
