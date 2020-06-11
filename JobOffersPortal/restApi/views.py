from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_auth.registration.views import RegisterView

from .serializers import JobAdvertisementSerializer, TagsSerializer
from .models import User, JobAdvertisement, Tag

class CustomRegisterView(RegisterView):
    queryset = User.objects.all()

class TagsList(APIView):
    serializer_class = TagsSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):

        tags = Tag.objects.all()
        serializer = TagsSerializer(tags, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = TagsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class JobAvertisementList(APIView):
    serializer_class = JobAdvertisementSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, format = None):
        jobs = JobAdvertisement.objects.all()
        serializer = JobAdvertisementSerializer(jobs, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = JobAdvertisementSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

