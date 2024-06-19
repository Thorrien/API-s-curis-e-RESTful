from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


from authentication.models import User, Contributor
from authentication.serializers import UserSerializer, ContributorSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()
