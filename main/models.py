from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='car_images', blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.car_name
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return '/media/no-image.png'