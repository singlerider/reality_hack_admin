from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions

from panel.models import Attendant, Project, AuthUser, Table, Team, RealityKit
from panel.serializers import AttendantSerializer, ProjectSerializer, AuthUserSerializer, GroupSerializer, TableSerializer, TeamSerializer, RealityKitSerializer


class AuthUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Auth Users to be viewed or edited.
    """
    queryset = AuthUser.objects.all().order_by('-date_joined')
    serializer_class = AuthUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttendantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Attendant to be viewed or edited.
    """
    queryset = Attendant.objects.all()
    serializer_class = AttendantSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Project to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tables to be viewed or edited.
    """
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class RealityKitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Reality Kits to be viewed or edited.
    """
    queryset = RealityKit.objects.all()
    serializer_class = RealityKitSerializer
