from django.db import models


# Create your models here.
class Image(models.Model):
    username = models.CharField(max_length=30, default="guest")
    photo = models.ImageField(upload_to="media")
    date = models.DateTimeField(auto_now_add=True)


class RegisterModel(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username
