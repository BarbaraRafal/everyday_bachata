from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import django_filters
# Create your models here.

class User(AbstractUser):
    pass

class Organizer(models.Model):
    organizer_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.organizer_name}"

class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return f" {self.city_name}"

class Trainers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)

EVENT_TYPES = [
    (1, "Workshops"),
    (2,"Festival"),
    (3,"Party")
]

class Events(models.Model):
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=100, null=True, blank=True)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    trainer = models.OneToOneField(Trainers, null=True, blank=True, on_delete=models.CASCADE)
    type = models.IntegerField(choices=EVENT_TYPES)

    def __str__(self):
        # return f"{EVENT_TYPES[self.type-1][1]}  w {self.city} dnia {self.start_date}"
        return f"{self.get_type_display()}  w {self.city} dnia {self.start_date}"

class EventsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Events
        fields = ['event_name', 'location']






