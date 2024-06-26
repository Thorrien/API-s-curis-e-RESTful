from rest_framework.serializers import ModelSerializer
from core.models import Project, Issue, Comment
from authentication.serializers import LightUserSerializer, LightContributorSerializer



class LightIssueSerializer(ModelSerializer):
    
    class Meta:
        model = Issue
        fields = ['id', 'title', 'statut']
        read_only_fields = ['author']


class ProjectDetailSerializer(ModelSerializer):

    author = LightUserSerializer(read_only=True, many=False)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['author']


class ProjectSerializer(ModelSerializer):    
    class Meta:
        model = Project
        fields = ['id', 'title']


class LightCommentSerializer(ModelSerializer):
    
    author = LightUserSerializer(read_only=True, many=False)
    
    class Meta:
        model = Comment
        fields = ['description', 'author']
        read_only_fields = ['author']
        

class CommentSerializer(ModelSerializer):
    author = LightUserSerializer(read_only=True)
    issue = LightIssueSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']

class IssueDetailSerializer(ModelSerializer):
    
    comments = LightCommentSerializer(read_only=True, many=True)
    worker = LightContributorSerializer(read_only=True, many=False)
    author = LightUserSerializer(read_only=True, many=False)
    project = ProjectSerializer(read_only=True, many=False)
    
    class Meta:
        model = Issue
        fields = ['id', 'created_time', 'updated_time', 'author', 'title', 'description', 'statut', 'priority', 'worker', 'type', 'project', 'comments']
        read_only_fields = ['author']

class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'created_time', 'author', 'title', 'project', 'description', 'statut', 'priority']

