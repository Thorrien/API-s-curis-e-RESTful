from rest_framework.serializers import ModelSerializer, ValidationError
from core.models import Project, Issue, Comment
from authentication.serializers import UserSerializer, ContributorSerializer

class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['author']


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'updated_time', 'title']


class LightCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_time', 'description', 'author']
        read_only_fields = ['author']
        

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']

class IssueDetailSerializer(ModelSerializer):
    
    comments = LightCommentSerializer(many=True)
    
    class Meta:
        model = Issue
        fields = ['id', 'created_time', 'updated_time', 'author', 'title', 'description', 'statut', 'priority', 'worker', 'type', 'project', 'comments']
        read_only_fields = ['author']

class IssueSerializer(ModelSerializer):
    
    class Meta:
        model = Issue
        fields = ['id', 'created_time', 'updated_time', 'author', 'title', 'description', 'statut', 'priority', 'worker', 'type', 'project']
        read_only_fields = ['author']
