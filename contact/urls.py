from django.urls import path
from .views import inquiry_request

urlpatterns = [

    path('inquiry', inquiry_request, name="inquiry_request")
]