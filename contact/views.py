import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from contact.serializers import ContactSerializer


@api_view(['POST'])
def inquiry_request(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        message = serializer.validated_data['message']

        send_mail(
            subject="customer inquiry",
            message=message,
            from_email=email,
            recipient_list=['business_email@example.com']
        )
        return Response({'status', 'success'}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
