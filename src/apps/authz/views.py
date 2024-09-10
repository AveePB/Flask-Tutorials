from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import login
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.conf import settings
import datetime

from apps.authz.forms import UsernamePasswordForm
from apps.accounts.models import User

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Fetch web page if not logged id
        if (request.user.is_anonymous):
            return render(request, 'auth_login.html')
        
        # Redirect if logged
        return redirect('/home/')

    def post(self, request, *args, **kwargs):
        # Fail if logged id
        if (not request.user.is_anonymous):
            return Response({'message': 'You\'re already logged in.'}, status.HTTP_403_FORBIDDEN)
        
        # Create and validate form
        form = UsernamePasswordForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Try to Log in            
            try:
                user = User.objects.get(username=username, password=password)
                login(request, user)

                # Set up cookie
                response = Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
                token = AccessToken.for_user(user)

                response.set_cookie(
                    settings.SIMPLE_JWT['AUTH_COOKIE'],
                    str(token),
                    expires=datetime.datetime.now(datetime.UTC) + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    httponly=True,
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )

                return response
            except User.DoesNotExist:
                return Response({'message': 'Invalid credentials.'}, status.HTTP_400_BAD_REQUEST)

        # Form doesn't match criteria    
        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Fetch web page if not logged id
        if (request.user.is_anonymous):
            return render(request, 'auth_register.html')
        
        # Redirect if logged
        return redirect('/home/')

    def post(self, request, *args, **kwargs):
        # Fail if logged id
        if (not request.user.is_anonymous):
            return Response({'message:', 'You\'re logged in, log out if you want to register a new account.'}, status.HTTP_403_FORBIDDEN)

        # Create and validate form
        form = UsernamePasswordForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Try to register           
            try:
                new_user = User(username=username, password=password)
                new_user.save(force_insert=True)
                return Response({'message': 'Registration successful.'}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'message': 'User already exists.'}, status.HTTP_409_CONFLICT)

        # Form doesn't match criteria    
        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        response = Response({'message': 'Successfully logged out.'}, status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
        return response