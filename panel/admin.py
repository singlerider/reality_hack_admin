from django.contrib import admin

from panel.models import Attendant, Project, RealityKit, Table, Team, AuthUser

admin.site.register(Attendant)
admin.site.register(AuthUser)
admin.site.register(Project)
admin.site.register(RealityKit)
admin.site.register(Table)
admin.site.register(Team)
