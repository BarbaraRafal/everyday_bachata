from django.urls import path
from bachata_app import views
from .views import SearchResultsView



app_name = 'bachata_app'

urlpatterns = [
    path('bachata_app/', views.bachata),
    path('list/', views.EventsListView.as_view(), name='events-list'),
    path('details/<int:pk>', views.EventsDetailView.as_view(), name='events-detail'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    ]
