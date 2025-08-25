from django.urls import path


from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenBlacklistView,
)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", CustomTokenBlacklistView.as_view(), name="token_blacklist"),
]
