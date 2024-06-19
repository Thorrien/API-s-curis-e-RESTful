from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from core.models import Project, Comment, Issue
from core.serializers import ProjectSerializer, IssueSerializer, CommentSerializer


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()
    
class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()
    
class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()