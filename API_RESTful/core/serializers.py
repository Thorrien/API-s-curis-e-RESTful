from rest_framework.serializers import ModelSerializer, ValidationError
from core.models import Project

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['created_time', 'updated_time', 'type', 'author', 'title', 'description']