from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


from authentication.models import User
from authentication.serializers import UserSerializer


class UserViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()