from django.db import models


# Create your models here.
class Car(models.Model):
    photo = models.ImageField(upload_to='cars_pictures', blank=True)
    name = models.CharField(max_length=100)
    # The first element in each tuple is the actual value to be set on the model, and the second element is the
    # human-readable name.
    # For example:
    CAR_TYPE_CHOICES = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Convertible', 'Convertible'),
        ('Minivan', 'Minivan'),
        ('Hatchback', 'Hatchback'),
        ('Crew Cab', 'Crew Cab'),
        ('Coupe', 'Coupe'),
        ('Regular Cab', 'Regular Cab'),
        ('Van', 'Van'),
        ('Wagon', 'Wagon'),
    )
    type = models.CharField(max_length=3, choices=CAR_TYPE_CHOICES)
    brand = models.CharField(max_length=100)
    num_of_passengers = models.IntegerField()
    price_per_day = models.IntegerField()
    air_conditioning = models.BooleanField()
    automatic_transmission = models.BooleanField()
    doors_4 = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = "rentalcar"
