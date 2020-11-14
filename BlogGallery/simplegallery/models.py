from django.db import models


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="gallery")
    captions = models.CharField(max_length=250, blank=True)
