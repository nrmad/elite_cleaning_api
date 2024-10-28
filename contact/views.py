import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from contact.serializers import ContactSerializer
from django_ratelimit.decorators import ratelimit


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
        return Response({'status', 'success'}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
