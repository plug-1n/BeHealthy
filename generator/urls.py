from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'generator'

urlpatterns = [
    path('', test, name="test")
]
