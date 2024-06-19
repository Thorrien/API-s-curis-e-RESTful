from rest_framework.serializers import ModelSerializer, ValidationError
from core.models import Project, Issue, Comment

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'created_time', 'updated_time', 'type', 'author', 'title', 'description']
        
        
class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'created_time', 'updated_time', 'type', 'author', 'title', 'description', 'project', 'statut', 'priority', 'worker']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_time', 'updated_time', 'author', 'author', 'issue', 'description', 'link']

