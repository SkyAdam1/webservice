from rest_framework import generics

from .models import Project
from .serializer import ProjectSerializer


class ProjectView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
