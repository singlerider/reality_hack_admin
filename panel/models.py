import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import OneToOneField
from django.utils.translation import gettext_lazy as _


class AuthUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Attendant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    core_competencies = models.CharField(max_length=100)
    participant = models.BooleanField(default=False)
    organizer = models.BooleanField(default=False)
    mentor = models.BooleanField(default=False)
    remote = models.BooleanField(default=False)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):

    class ProjectCategories(models.TextChoices):
        OPTION_ONE = 'OO', _('Option One')
        OPTION_TWO = 'OT', _('Option Two')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    category = models.CharField(
        max_length=2,
        choices=ProjectCategories.choices,
        default=ProjectCategories.OPTION_ONE,
    )
    repository = models.CharField(max_length=255)
    submitted_by = models.ForeignKey(Attendant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Table(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Table number {self.number} at {self.location}"


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(Attendant)
    tables = models.ManyToManyField(Table)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RealityKit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255)
    table = OneToOneField(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.table}, at {self.address}"

    class Meta:
        verbose_name = 'Reality Kit'
        verbose_name_plural = 'Reality Kits'
