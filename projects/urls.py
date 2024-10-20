# projects/urls.py

from django.urls import path
from .views import project_detail, sector_projects

urlpatterns = [
    path('sectors/<int:sector_id>', sector_projects, name="sector_projects"),
    path('<int:project_id>', project_detail, name="project_detail")
]