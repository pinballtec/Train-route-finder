from django.db import models
from django.core.exceptions import ValidationError
from cities.models import City
# Create your models here.


class Trains(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Train number')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel Time')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_set', verbose_name='arrival city')
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_set', verbose_name='departure city')

    def __str__(self):
        return self.name

    """Stable functions for processing and filtering objects from the model(clean/save)"""
    def clean(self):
        if self.arrival_city == self.departure_city:
            raise ValidationError('Wrong city from input')
        qs = Trains.objects.filter(
            arrival_city=self.arrival_city, departure_city=self.departure_city,
            travel_time = self.travel_time
        ).exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError('Wrong time from input')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)