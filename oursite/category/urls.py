from django.urls import path
from .views import wear,turism,electronics,forhome,create

urlpatterns = [
    path('forhome',forhome),
    path('wear',wear),
    path('turism',turism),
    path('electronics',electronics),
    path('create',create)
]


