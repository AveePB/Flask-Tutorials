from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from apps.accounts.models import User
from apps.accounts.forms import *
from apps.networks.models import Follow
import uuid

# Create your views here.
class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        form = UsernameForm(request.POST)
        if (form.is_valid()):
            follower = User.objects.get(id=request.user.id)
            username = form.cleaned_data['username']

            try:
                # Start following a user
                user = User.objects.get(username=username)
                follow = Follow(user=user, follower=follower)
                follow.save(force_insert=True)
                return Response({'message': 'Successfully started following.'}, status.HTTP_201_CREATED)
            
            except ValidationError:
                return Response({'message': 'You cannot follow yourself.'}, status.HTTP_403_FORBIDDEN)

            except IntegrityError:
                return Response({'message': 'You already follow that user.'}, status.HTTP_204_NO_CONTENT)
            
            except User.DoesNotExist:
                return Response({'message': 'User doesn\'t exist.'}, status.HTTP_404_NOT_FOUND)

        return Response({'message': form.errors.as_text()}, status.HTTP_400_BAD_REQUEST)
    

class UnFollowView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, username):
        follower = User.objects.get(id=request.user.id)

        try:
            user = User.objects.get(username=username)
            follow = Follow.objects.get(follower=follower, user=user)
            follow.delete()
            return Response({'message': 'You stopped following that user'}, status.HTTP_204_NO_CONTENT)
        
        except User.DoesNotExist:
            return Response({'message': 'User doesn\'t exist.'}, status.HTTP_204_NO_CONTENT)
        
        except Follow.DoesNotExist:
            return Response({'message': 'You didn\'t follow that user.'}, status.HTTP_204_NO_CONTENT)