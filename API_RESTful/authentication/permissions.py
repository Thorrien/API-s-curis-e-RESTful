from rest_framework.permissions import BasePermission, SAFE_METHODS
from authentication.models import Contributor


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(user=request.user, project=obj.project).exists()


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or obj.can_be_shared == True


class IsOnProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(user=request.user, project=obj).exists() or obj.author == request.user


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class IsOnProjectIssue(BasePermission):

    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(user=request.user, project=obj.project).exists() or obj.author == request.user


class IsOnProjectComment(BasePermission):

    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(user=request.user, project=obj.issue.project).exists() or obj.author == request.user
