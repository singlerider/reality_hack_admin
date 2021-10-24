from django.contrib import admin
from django.urls import path
from rest_framework import routers
from panel import views

router = routers.DefaultRouter()
router.register(r'authusers', views.AuthUserViewSet)
router.register(r'attendants', views.AttendantViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'tables', views.TableViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'realitykits', views.RealityKitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
