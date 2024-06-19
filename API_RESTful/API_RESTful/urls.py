"""
URL configuration for API_RESTful project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from authentication.views import UserViewset, ContributorViewset
from core.views import ProjectViewset, IssueViewset, CommentViewset

router = routers.SimpleRouter()

router.register('user', UserViewset, basename='user')
router.register('projet', ProjectViewset, basename='projet')
router.register('contributeur', ContributorViewset, basename='contributeur')
router.register('ticket', IssueViewset, basename='ticket')
router.register('commentaire', CommentViewset, basename='commentaire')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
