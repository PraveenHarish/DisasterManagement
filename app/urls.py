from django.urls import path
from . import views

urlpatterns = [

    path("", views.home),
    path("disasters/", views.disasters),
    path("preparedness/", views.preparedness),
    path("shelters/", views.shelters),
    path("contacts/", views.contacts),
    path("report/", views.report),

]