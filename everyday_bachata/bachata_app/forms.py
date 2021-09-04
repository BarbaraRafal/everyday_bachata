from django import forms

from .models import Events

# Formularz modelu

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['city', 'type']
        labels = {"city": "Miasto", "type": "Rodzaj wydarzenia"}
