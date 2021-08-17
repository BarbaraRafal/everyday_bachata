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
    organizer_address = models.CharField(max_length=50)

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


class EventType(models.Model):
    event_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.event_type}"

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField
    location = models.CharField(max_length=50)
    price = models.IntegerField(max_length=10)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=100)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)






