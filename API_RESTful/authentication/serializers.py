from rest_framework.serializers import ModelSerializer, ValidationError
from authentication.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'age']

    def validate(self, data):
        if data['age'] < 14 :
            raise ValidationError('Personne trop jeune')
        return data