from rest_framework.viewsets import ModelViewSet
from authentication.models import User, Contributor
from authentication.serializers import UserSerializer, ContributorSerializer, UserDetailSerializer
from authentication.permissions import IsUser, IsAdminAuthenticated


class UserViewset(ModelViewSet):

    permission_classes = [IsAdminAuthenticated]
    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsUser]
        return super().get_permissions()


class ContributorViewset(ModelViewSet):

    permission_classes = [IsAdminAuthenticated]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()
