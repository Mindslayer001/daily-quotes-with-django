from django.urls import path
from .views import getRandomQuotation

urlpatterns = [
    path("", getRandomQuotation)
]
