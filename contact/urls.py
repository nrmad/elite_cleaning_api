from django.urls import path
from .views import inquiry_request, verify_recaptcha

urlpatterns = [

    path('inquiry', inquiry_request, name="inquiry_request"),
    path('verify', verify_recaptcha, name='verify_recaptcha')
]