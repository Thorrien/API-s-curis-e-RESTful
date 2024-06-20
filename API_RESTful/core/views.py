from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from core.models import Project, Comment, Issue
from core.serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ProjectDetailSerializer


class ProjectViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()
    
    def get_serializer_class(self):
    # Si l'action demandée est retrieve nous retournons le serializer de détail
        if self.action == 'retrieve' :
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    
class IssueViewset(ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()
    
class CommentViewset(ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()