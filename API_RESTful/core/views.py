from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Project, Comment, Issue
from authentication.models import Contributor, User
from authentication.serializers import LightContributorSerializer
from core.serializers import ProjectSerializer, IssueSerializer, IssueDetailSerializer, CommentSerializer, ProjectDetailSerializer
from authentication.permissions import IsOnProject, IsAdminAuthenticated, IsAuthor, IsOnProjectComment, IsOnProjectIssue, IsContributor
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status


class ProjectViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsOnProject]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAuthor]
        elif self.action == 'create':
            self.permission_classes = [IsAdminAuthenticated]
        return super().get_permissions()

    @action(detail=False, methods=['post'],
            permission_classes=[IsAuthenticated])
    def newprojet(self, request):
        data = request.data.copy()
        serializer = ProjectSerializer(data=data)

        if serializer.is_valid():
            project = serializer.save(author=request.user)
            Contributor.objects.create(user=request.user,
                                       project=project)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'],
            permission_classes=[IsOnProject])
    def tickets(self, request, pk=None):
        project = self.get_object()
        tickets = Issue.objects.filter(project=project)
        serializer = IssueSerializer(tickets, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'],
            permission_classes=[IsOnProject])
    def contributeurs(self, request, pk=None):
        project = self.get_object()
        contributors = Contributor.objects.filter(project=project)
        serializer = LightContributorSerializer(contributors,
                                                many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'],
            permission_classes=[IsAuthenticated, IsOnProject])
    def newticket(self, request, pk=None):
        project = self.get_object()
        data = request.data.copy()
        data['project'] = project.id
        data['author'] = request.user.id
        serializer = IssueSerializer(data=data)

        if serializer.is_valid():
            issue = serializer.save(author=request.user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'],
            url_path='tickets/(?P<ticket_pk>[^/.]+)',
            permission_classes=[IsAuthenticated, IsOnProject])
    def ticket_detail(self, request, pk=None, ticket_pk=None):
        project = self.get_object()
        try:
            ticket = Issue.objects.get(pk=ticket_pk, project=project)
        except Issue.DoesNotExist:
            return Response({'detail': 'Ticket not found'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = IssueSerializer(ticket)
        return Response(serializer.data)

    @action(detail=True, methods=['post'],
            url_path='tickets/(?P<ticket_pk>[^/.]+)/newcommentaire',
            permission_classes=[IsAuthenticated, IsOnProject])
    def newcommentaire(self, request, pk=None, ticket_pk=None):
        project = self.get_object()
        try:
            ticket = Issue.objects.get(pk=ticket_pk, project=project)
        except Issue.DoesNotExist:
            return Response({'detail': 'Ticket not found'},
                            status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['issue'] = ticket.id
        data['author'] = request.user.id
        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            user = User.objects.get(id=request.user.id)
            comment = serializer.save(author=user, issue=ticket)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'],
            url_path='tickets/(?P<ticket_pk>[^/.]+)/commentaires',
            permission_classes=[IsAuthenticated, IsOnProject])
    def commentaires(self, request, pk=None, ticket_pk=None):
        try:
            ticket = Issue.objects.get(pk=ticket_pk, project_id=pk)
        except Issue.DoesNotExist:
            return Response({'detail': 'Ticket not found'},
                            status=status.HTTP_404_NOT_FOUND)

        comments = Comment.objects.filter(issue=ticket)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(
        detail=True, methods=['get'],
        url_path='tickets/(?P<ticket_pk>[^/.]+)/commentaires/(?P<comment_pk>[^/.]+)',
        permission_classes=[IsAuthenticated, IsOnProjectIssue]
        )
    def comment_detail(self, request, pk=None, ticket_pk=None,
                       comment_pk=None):
        try:
            comment = Comment.objects.get(pk=comment_pk,
                                          issue__pk=ticket_pk,
                                          issue__project_id=pk)
        except Comment.DoesNotExist:
            return Response({'detail': 'Commentaire not found'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IssueViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = IssueSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        projects = Contributor.objects.filter(
            user=self.request.user
            ).values_list('project', flat=True)
        return Issue.objects.filter(project__in=projects)

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsOnProjectIssue]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAuthor]
        elif self.action == 'create':
            self.permission_classes = [IsAdminAuthenticated]
        return super().get_permissions()

    @action(detail=True, methods=['get'],
            permission_classes=[IsContributor])
    def commentaires(self, request, pk=None):
        issue = self.get_object()
        comments = Comment.objects.filter(issue=issue)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = CommentSerializer

    def get_queryset(self):
        projects = Contributor.objects.filter(
            user=self.request.user
            ).values_list('project', flat=True)
        issues = Issue.objects.filter(project__in=projects)
        return Comment.objects.filter(issue__in=issues)

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsOnProjectComment]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAuthor]
        elif self.action == 'create':
            self.permission_classes = [IsAdminAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PersonalIssueViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueSerializer
    detail_serializer_class = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.filter(
            worker__user=self.request.user
            ).exclude(statut='Terminé')

    @action(detail=True, methods=['get'],
            permission_classes=[IsAuthenticated])
    def commentaires(self, request, pk=None):
        issue = self.get_object()
        comments = Comment.objects.filter(issue=issue)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAuthor]
        elif self.action == 'create':
            self.permission_classes = [IsAdminAuthenticated]
        return super().get_permissions()

    @action(detail=True, methods=['post'],
            url_path='newcommentaire',
            permission_classes=[IsAuthenticated, IsOnProject])
    def newcommentaire(self, request, pk=None):
        try:
            ticket = Issue.objects.get(
                pk=pk,
                worker__user=self.request.user
                )
        except Issue.DoesNotExist:
            return Response({'detail': 'Ticket not found'},
                            status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['issue'] = ticket.id
        data['author'] = request.user.id
        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            user = User.objects.get(id=request.user.id)
            comment = serializer.save(author=user, issue=ticket)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'],
            url_path='commentaires/(?P<comment_pk>[^/.]+)',
            permission_classes=[IsAuthenticated, IsOnProjectIssue])
    def comment_detail(self, request, pk=None, comment_pk=None):
        ticket = self.get_object()
        try:
            comment = Comment.objects.get(pk=comment_pk)
        except Issue.DoesNotExist:
            return Response({'detail': 'Commentaire not found'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(ticket)
        return Response(serializer.data)
