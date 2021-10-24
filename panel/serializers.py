from django.contrib.auth.models import Group
from panel.models import Attendant, Project, RealityKit, Table, Team, AuthUser
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group
        fields = ['url', 'name']


class AuthUserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = AuthUser
        fields = ['url']


class AttendantSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Attendant
        fields = [
            'url', 'first_name', 'last_name', 'core_competencies',
            'participant', 'organizer', 'mentor', 'bio'
        ]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Project
        fields = [
            'url', 'name', 'category', 'repository', 'submitted_by'
        ]


class RealityKitSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = RealityKit
        fields = [
            'url', 'address', 'table'
        ]


class TableSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Table
        fields = [
            'url', 'number', 'location'
        ]


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    tables = TableSerializer(many=True)

    class Meta:
        model = Team
        fields = [
            'url', 'participants', 'tables', 'repository'
        ]
