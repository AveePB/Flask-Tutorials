from django.urls import path
from apps.accounts.views import *

urlpatterns = [
    path('username/', UsernameView.as_view(), name='username'),
    path('password/', PasswordView.as_view(), name='password'),
    
    path('avatar/', AvatarView.as_view(), name='avatar'),
    path('background/', BackgroundView.as_view(), name='background'),
    path('bio/', BioView.as_view(), name='bio'),
    
    path('skills/', SkillsView.as_view(), name='skills'),
    path('skills/<str:skill_uuid>/', DeleteSkillsView.as_view(), name='delete_skills'),
]