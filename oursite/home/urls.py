from django.urls import path
from .views import index, about, category, contact

urlpatterns = [
    path('', index),
    path('index', index),
    path('about', about),
    path('contact', contact),
    path('category', category)
]