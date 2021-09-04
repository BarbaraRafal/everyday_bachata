from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import reverse

from .forms import EventsForm


from .models import Events


# Create your views here.
def bachata(request):

    if request.method == "POST":

        city = request.POST.get('city')
        type = request.POST.get('type')

        return redirect(reverse('bachata_app:results',args= [city,type]))

    form = EventsForm()

    return render(
        request, 'bachata_app/bachata.html',
        context={
            "form": form, "events": []
        }
    )

def results(request, city,type):
    form = EventsForm()
    events = Events.objects.filter(city=city, type=type)
    return render(
        request, 'bachata_app/bachata.html',
        context={
            "form":form, "events":events
        }
    )


class EventsListView(ListView):
    model = Events

class EventsDetailView(DetailView):
    model = Events



class SearchResultsView(ListView):
    model = Events
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Events.objects.filter(
            Q(city__icontains=query)|Q(type__icontains=query))
        return object_list
