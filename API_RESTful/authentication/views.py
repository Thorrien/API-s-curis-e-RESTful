from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


from authentication.models import User, Contributor
from authentication.serializers import UserSerializer, ContributorSerializer, UserDetailSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer

    def get_queryset(self):
        return User.objects.all()
    
    def get_serializer_class(self):
    # Si l'action demandée est retrieve nous retournons le serializer de détail
        if self.action == 'retrieve' :
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()


