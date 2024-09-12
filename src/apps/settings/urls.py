from django.urls import path
from apps.settings.views import *

urlpatterns = [
    path('', SettingsView.as_view(), name='settings'),
    path('account-data/', AccountDataView.as_view(), name='account-data'),
    path('profile-data/', ProfileDataView.as_view(), name='profile-data'),
    path('profile-images/', ProfileImagesView.as_view(), name='profile-images'),
]