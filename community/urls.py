
from django.urls import path, re_path
from .views import home

urlpatterns = [
    path('<str:name>', home),
]

