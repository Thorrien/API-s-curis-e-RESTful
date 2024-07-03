from rest_framework.serializers import ModelSerializer, ValidationError
from authentication.models import User, Contributor


class LightUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class UserSerializer(ModelSerializer):    
    class Meta:
        model = User
        fields = ['id', 'username', 'age']

    def validate(self, data):
        if data['age'] < 14:
            raise ValidationError('Personne trop jeune')
        return data


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project']


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'age',
                  'can_be_contacted',
                  'can_data_be_shared',
                  'is_active']


class LightContributorSerializer(ModelSerializer):

    user = LightUserSerializer(read_only=True)

    class Meta:
        model = Contributor
        fields = ['user']
