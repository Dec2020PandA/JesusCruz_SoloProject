from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('contact', views.contact),
    path('gallery', views.gallery),
    path('form', views.form)
]