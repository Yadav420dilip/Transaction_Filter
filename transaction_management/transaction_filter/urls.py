from django.urls import path, include
from .views import transaction_details

urlpatterns = [
    path('', transaction_details)
]
