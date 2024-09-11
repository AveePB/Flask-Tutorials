from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

from apps.accounts.models import User, Skill
from apps.accounts.forms import *
import uuid

# Create your views here.
class UsernameView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Create and process form
        form = UsernameForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            user = User.objects.get(id=request.user.id)
            
            # Try to change username
            try:
                user.username = username
                user.save(force_update=True)
                return Response({'message': 'Username successfully updated.'}, status.HTTP_204_NO_CONTENT)
            except IntegrityError:
                return Response({'message': 'Username is alredy taken.'}, status.HTTP_400_BAD_REQUEST)

        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)            

class PasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Create and process form
        form = PasswordForm(request.POST)
        if (form.is_valid()):
            password = form.cleaned_data['password']
            user = User.objects.get(id=request.user.id)
            
            # Try to change password
            user.password = password
            user.save(force_update=True)
            return Response({'message': 'Password successfully updated.'}, status.HTTP_204_NO_CONTENT)

        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)        
    
class AvatarView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        # Check if there more than one file
        if (len(request.FILES) > 1):
            return Response({'message': 'Please upload exactly one image file.'}, status.HTTP_400_BAD_REQUEST)

        # Create and process form
        form = AvatarForm(request.POST, files=request.FILES)
        if (form.is_valid()):
            avatar = form.cleaned_data['file']
            user = User.objects.get(id=request.user.id)
            
            # Delete previous avatar
            if (user.avatar):
                user.avatar.delete(save=False)
            
            # Generate custom name
            ext = avatar.name.split('.')[-1]
            new_filename = f"{uuid.uuid4().hex}.{ext}"
            
            # Try to change avatar
            user.avatar.save(new_filename, avatar)
            user.save(force_update=True)
            return Response({'message': 'Avatar successfully uploaded.'}, status.HTTP_204_NO_CONTENT)

        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, *args, **kwargs):
        # Get user data
        user = User.objects.get(id=request.user.id)

        # Delete current avatar
        user.avatar.delete(save=False)
        user.save(force_update=True)

        return Response({'message': 'Avatar successfully deleted.'}, status.HTTP_204_NO_CONTENT)         

class BioView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Create and process form
        form = BioForm(request.POST)
        if (form.is_valid()):
            bio = form.cleaned_data['bio']
            
            # Try to change bio
            user = User.objects.get(id=request.user.id)
            user.bio = bio
            user.save(force_update=True)
            return Response({'message': 'Bio successfully updated.'}, status.HTTP_204_NO_CONTENT)

        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)        
    
    def delete(self, request, *args, **kwargs):
        # Get user data
        user = User.objects.get(id=request.user.id)

        # Delete current bio
        user.bio = ""
        user.save(force_update=True)

        return Response({'message': 'Bio successfully deleted.'}, status.HTTP_204_NO_CONTENT)       

class SkillsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Create and process form
        form = SkillForm(request.POST)
        if (form.is_valid()):
            skill_name = form.cleaned_data['skill_name']
            user = User.objects.get(id=request.user.id)
            
            # Try to add new skill
            try:
                new_skill = Skill(name=skill_name, user=user)
                new_skill.save(force_insert=True)
                return Response({'message': 'Skills successfully added.'}, status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({'message': 'Skill cannot be added.'}, status.HTTP_400_BAD_REQUEST)

        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)            

class DeleteSkillsView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, skill_uuid):
        try:
            user = User.objects.get(id=request.user.id)
            skill = Skill.objects.get(uuid=skill_uuid, user=user)
            
            skill.delete()
            return Response({'message': 'Skill successfully deleted.'}, status.HTTP_204_NO_CONTENT)
        except Skill.DoesNotExist:
            return Response({'message': 'There was no such skill.'}, status.HTTP_204_NO_CONTENT)

