from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tag, JobAdvertisement, User
from rest_auth.registration.views import RegisterView
from rest_framework.permissions import IsAuthenticated

class CustomRegisterView(RegisterView):
    queryset = User.objects.all()