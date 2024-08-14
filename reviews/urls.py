# reviews/urls.py

from django.urls import path
from .views import review_list

urlpatterns = [
    path('', review_list, name='review-list'),
]