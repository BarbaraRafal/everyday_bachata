from django.db import models

# Create your models here.

class UserType(models.Model):
    user_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user_type}"


class User(models.Model):
     login = models.CharField(max_length=50)
     password = models.CharField(max_length=8)
     email= models.CharField(max_length=50)
     type = models.OneToOneField(UserType, on_delete=models.CASCADE)

     def __str__(self):
         return f"{self.login} , {self.email}"


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
    trainer = models.ManyToManyField(Trainers, null=True, blank=True)
    type = models.IntegerField(choices=EVENT_TYPES)

    def __str__(self):
        return f"{self.event_name} dnia {self.start_date} w {self.city}"






