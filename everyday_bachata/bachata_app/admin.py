from django.contrib import admin
from bachata_app.models import Organizer
from bachata_app.models import City
from bachata_app.models import Trainers
from bachata_app.models import Events
from bachata_app.models import User
from bachata_app.models import UserType


# Register your models here.
admin.site.register(Organizer)
admin.site.register(City)
admin.site.register(Trainers)
admin.site.register(Events)
admin.site.register(User)
admin.site.register(UserType)


