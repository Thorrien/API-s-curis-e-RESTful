from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from core.models import Project
from core.serializers import ProjectSerializer


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()