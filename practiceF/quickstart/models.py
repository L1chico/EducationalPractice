from django.db import models

# Create your models here.
class user_image(models.Model):
    title = models.CharField(max_length=20,blank=True)
    image_downloaded = models.ImageField(upload_to='image_downloaded/')
    def __str__(self):
        return f'{self.title}'