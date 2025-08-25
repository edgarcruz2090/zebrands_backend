from rest_framework import routers
from django.urls import path

from apps.users.views.v1.user import AdminUserViewSet

router = routers.DefaultRouter()
router.register(r"", AdminUserViewSet, basename="users")

urlpatterns = router.urls
