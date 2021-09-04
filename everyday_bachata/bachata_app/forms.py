from django import forms

from bachata_app.models import Events

# Formularz modelu

class EventsForm(forms.Form):
    class Meta:
        model = Events
        fields = 'city'
        labels = {"city": "Miasto"}
