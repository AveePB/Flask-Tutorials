from django.urls import path
from apps.settings.views import *

urlpatterns = [
    path('', SettingsView.as_view(), name='settings'),
    path('account-data/', AccountDataView.as_view(), name='account-data'),
]