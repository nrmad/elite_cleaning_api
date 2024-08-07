# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from common.serializers import GenericSerializer

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = GenericSerializer(reviews, many=True)
    return Response(serializer.data)