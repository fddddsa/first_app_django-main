from django.urls import path
from django.contrib import admin
from firstapp import views
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
]