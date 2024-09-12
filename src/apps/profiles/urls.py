from django.urls import path
from apps.profiles.views import *

urlpatterns = [
    path('', ProfileRedirectView.as_view(), name='profile_redirect'),
    path('<str:user_uuid>/', ProfileView.as_view(), name='profile'),
]