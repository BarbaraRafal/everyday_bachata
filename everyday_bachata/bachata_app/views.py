from django.shortcuts import render

# Create your views here.
def bachata(request):
    return render(
        request, 'bachata.html'
    )
