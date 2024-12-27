import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from contact.serializers import ContactSerializer
from django_ratelimit.decorators import ratelimit
from django.conf import settings
import requests


@ratelimit(key='ip', rate='5/m', method=ratelimit.UNSAFE, block=True)
@api_view(['POST'])
def inquiry_request(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        message = serializer.validated_data['message']

        send_mail(
            subject="customer inquiry",
            message=f"Message from: {email}\n\n{message}",
            from_email="info@cleanelite.co.uk",
            recipient_list=['info@cleanelite.co.uk']
        )
        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


@ratelimit(key='ip', rate='5/m', method=ratelimit.UNSAFE, block=True)
@api_view(['POST'])
def verify_recaptcha(request):
    token = request.data.get('captcha')
    if not token:
        return Response({'error': 'Captcha token is required'}, status=status.HTTP_400_BAD_REQUEST)

    response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': token
        }
    )

    result = response.json()
    if result.get('success'):
        return Response({'success': True}, status=status.HTTP_200_OK)

    return Response({'error': 'Captcha verification failed'}, status=status.HTTP_400_BAD_REQUEST)