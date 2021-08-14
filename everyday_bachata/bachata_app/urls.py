from django.urls import path

from bachata_app import views

urlpatterns = [
    path('bachata_app/', views.bachata),
    ]