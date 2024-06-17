from django.db import models
from django.conf import settings
from authentication.models import Contributor
import uuid

class Project(models.Model):
    
    BACK = 'back-end'
    FRONT = 'front-end'
    IOS = 'iOS'
    ANDROID = 'Android'
    TYPE_PROJECTS = [
        (BACK, 'back-end'),
        (FRONT, 'front-end'),
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    ]
    
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Contributor, related_name='Contributeurs', blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=1000)
    type = models.CharField(max_length=20, choices=TYPE_PROJECTS )
    

class Issue(models.Model):
    
    LOW = 'Faible'
    MEDIUM = 'Moyenne'
    HIGH = 'Forte'
    CRITICAL = 'Critique'
    BUG = 'Bug'
    FEATURE = 'Fonctionnalité'
    TASK = 'Tâche'
    TO_DO = 'A faire'
    IN_PROGRESS = 'En cours'
    FINSHED = 'Terminé'

    TYPE_PRIORITY = [
        (LOW, 'Faible'),
        (MEDIUM, 'Moyenne'),
        (HIGH, 'Forte'),
        (CRITICAL, 'Critique'),
    ]

    TYPE_ISSUE = [
        (BUG, 'Bug'),
        (FEATURE, 'Fonctionnalité'),
        (TASK, 'Tâche'),
    ]

    STATUS_ISSUE = [
        (TO_DO, 'A faire'),
        (IN_PROGRESS, 'En cours'),
        (FINSHED, 'Terminé'),
    ]

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=1000)
    statut = models.CharField(max_length=20, choices=STATUS_ISSUE, default=TO_DO )
    priority = models.CharField(max_length=20, choices=TYPE_PRIORITY, default=LOW )
    worker = models.ForeignKey(Contributor, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_ISSUE )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE,  null=True,)
    description = models.TextField(blank=True, max_length=1000)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(max_length=300,  null=True,)