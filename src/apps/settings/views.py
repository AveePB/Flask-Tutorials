from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.conf import settings

from apps.accounts.models import User, Skill

# Create your views here.
class SettingsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Redirect to login page if not logged in
        if (request.user.is_anonymous):
            return redirect('/auth/login/')

        # Get user avatar
        current_user = User.objects.get(id=request.user.id)
        
        if (current_user.avatar):
            avatar_url = current_user.avatar.url
        else:
            avatar_url = '/media/unknown.png'

        return render(request, 'settings.html', {
            'user': current_user, 
            'avatar_url': avatar_url
        })

class AccountDataView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Redirect to login page if not logged in
        if (request.user.is_anonymous):
            return redirect('/auth/login/')
        
        # Get user avatar
        current_user = User.objects.get(id=request.user.id)

        return render(request, 'settings_account_data.html', {
            'current_username': current_user.username,
        })

class ProfileDataView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Redirect to login page if not logged in
        if (request.user.is_anonymous):
            return redirect('/auth/login/')
        
        # Get user data
        current_user = User.objects.get(id=request.user.id)
        
        return render(request, 'settings_profile_data.html', {
            'current_bio': current_user.bio,
            'skills': Skill.objects.filter(user=current_user),
        })