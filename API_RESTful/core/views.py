from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Project, Comment, Issue
from authentication.models import Contributor
from core.serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ProjectDetailSerializer
from authentication.permissions import IsOnProject, IsAuthor, IsContributor
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class ProjectViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve' :
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsOnProject]
        return super().get_permissions()
    
    @action(detail=True, methods=['get'], permission_classes=[IsOnProject])
    def tickets(self, request, pk=None):
        project = self.get_object()
        tickets = Issue.objects.filter(project=project)
        serializer = IssueSerializer(tickets, many=True)
        return Response(serializer.data)


class IssueViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsContributor]
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def commentaires(self, request, pk=None):
        issue = self.get_object()
        comments = Comment.objects.filter(issue=issue)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    
class CommentViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class PersonalIssueViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(worker__user=self.request.user).exclude(statut='Terminé')

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def commentaires(self, request, pk=None):
        issue = self.get_object()
        comments = Comment.objects.filter(issue=issue)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)