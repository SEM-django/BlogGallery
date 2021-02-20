from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="gallery")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.title


class Choosen_One(models.Model):
    theme = models.CharField(max_length=100)
