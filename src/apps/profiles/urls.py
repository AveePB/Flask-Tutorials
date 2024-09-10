from django.urls import path
from apps.profiles.views import ProfileView, ProfileRedirectView

urlpatterns = [
    path('<str:user_uuid>/', ProfileView.as_view(), name='profile'),
    path('', ProfileRedirectView.as_view(), name='profile_redirect'),
]