from django.db import models
from cities.models import City
from trains.models import Trains
# Create your models here.


class Rotes(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Train number')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Travel Time')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_city_set_rotes_model', verbose_name='arrival city_rotes_model')
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_city_set_rotes_model', verbose_name='departure city_rotes_model')
    trains = models.ManyToManyField(Trains, verbose_name='trains list')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['travel_times']