from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('departments/', department),
    path('doctor/', doctors),
    path('booking/',booking)
]
