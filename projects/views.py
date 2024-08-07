# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project
from common.serializers import GenericSerializer
from rest_framework.pagination import PageNumberPagination
from .serializers import SectorProjectSerializer, ProjectSerializer
from rest_framework.exceptions import NotFound



class CustomPagination(PageNumberPagination):
    page_size = 6
    page_size_query_aram = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def sector_projects(request):
    sector_id = request.query_params.get('sector_id')
    projects = Project.objects.filter(sector_id=sector_id).prefetch_related('media').only('title')

    # Pagination
    paginator = CustomPagination()
    paginated_projects = paginator.paginate_queryset(projects, request)

    # Serialize the data
    serializer = SectorProjectSerializer(paginated_projects, many=True)
    return Response(paginator.get_paginated_response(serializer.data))


@api_view(['GET'])
def project_detail(request, project_id):

    try:
        project = Project.objects.prefetch_related('media').get(pk=project_id)
    except Project.DoesNotExist:
        raise NotFound('Project not found')

    serializer = ProjectSerializer(project)
    return Response(serializer.data)