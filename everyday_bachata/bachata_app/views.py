from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Events, EventsFilter


# Create your views here.
def bachata(request):
    return render(
        request, 'bachata_app/bachata.html'
    )

class EventsListView(ListView):
    model = Events

class EventsDetailView(DetailView):
    model = Events

def Filter_list(request):
    f = EventsFilter(request.GET, queryset=Events.objects.all())
    return render(
        request, 'bachata_app/events_filter.html', {'filter': f}
    )

