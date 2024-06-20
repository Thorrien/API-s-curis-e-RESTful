from rest_framework.serializers import ModelSerializer, ValidationError
from authentication.models import User, Contributor

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

    def validate(self, data):
        if data['age'] < 14 :
            raise ValidationError('Personne trop jeune')
        return data
    
    
class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project']


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "password", 'age', 'can_be_contacted', 'can_be_shared']
