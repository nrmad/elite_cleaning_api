# projects/urls.py

from django.urls import path
from .views import project_detail, sector_projects

urlpatterns = [
    path('sectors/<int:sector_id/projects', sector_projects, name="sector_projects"),
    path('sectors/<int:sector_id>/projects/<int:id>', project_detail, name="project_detail")
]