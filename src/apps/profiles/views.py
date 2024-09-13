from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.conf import settings

from apps.accounts.models import *

# Create your views here.
class ProfileRedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Redirect to login page if not logged in
        if (request.user.is_anonymous):
            return redirect('/auth/login/')
        
        return redirect(f'/profiles/{request.user.uuid}/')

class ProfileView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, user_uuid):
        # Redirect to login page if not logged in
        if (request.user.is_anonymous):
            return redirect('/auth/login/')
        
        current_user = User.objects.get(id=request.user.id)
        
        try:
            accessed_user = User.objects.get(uuid=user_uuid)
            skills = Skill.objects.filter(user=accessed_user)

            return render(request, 'profile.html', context={
                'user': accessed_user,
                'skills': skills,
                'avatar_url': accessed_user.get_avatar_url(),
                'background_url': accessed_user.get_background_url(),
                'is_following': Follow.objects.filter(user=accessed_user, follower=current_user).exists(),
                'is_own_profile': current_user.uuid == accessed_user.uuid,
            })
        except User.DoesNotExist:
            return Response({'message': 'User doesn\'t exist.'}, status.HTTP_404_NOT_FOUND)
        

        
