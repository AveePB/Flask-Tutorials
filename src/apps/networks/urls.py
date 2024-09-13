from django.urls import path
from apps.networks.views import *

urlpatterns = [
    path('follow/', FollowView.as_view(), name='follow'),
    path('unfollow/<str:username>/', UnFollowView.as_view(), name='unfollow'),
]