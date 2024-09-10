from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect, render

from apps.accounts.models import User

# Create your views here.
class ProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_uuid):
        # Redirect to login page if not logged in
        if (request.user.is_anonymous):
            return redirect('/auth/login/')

        try:
            # Fetch user data
            user = User.objects.get(uuid=user_uuid)
            if (user.avatar):
                avatar_url = user.avatar.url
            else:
                avatar_url = '/media/unknown.png'
    
            return render(request, 'profile.html', {'user': user, 'avatar_url': avatar_url})
        except User.DoesNotExist:
            return Response({'message': 'Invalid profile link.'}, status.HTTP_404_NOT_FOUND)
        
class ProfileRedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Redirect to login page if not logged in
        if (request.user.is_anonymous):
            return redirect('/auth/login/')
        
        user = User.objects.get(id=request.user.id)
        return redirect(f'/profiles/{user.uuid}/')