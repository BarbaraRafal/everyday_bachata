from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q

from .forms import EventsForm


from .models import Events


# Create your views here.
def bachata(request):
    return render(
        request, 'bachata_app/bachata.html'
    )


class EventsListView(ListView):
    model = Events

class EventsDetailView(DetailView):
    model = Events

class SearchResultsView(ListView):
    model = Events
    template_name = 'search-results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Events.objects.filter(
            Q(city__icontains=query)|Q(type__icontains=query))
        return object_list

# def search_result(request):
#     pass