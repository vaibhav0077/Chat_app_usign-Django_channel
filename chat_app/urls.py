from django.contrib import admin
from django.urls import path
from .views import messages_page

urlpatterns = [
    path('', messages_page),
]
