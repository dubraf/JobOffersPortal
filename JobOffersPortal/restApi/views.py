from rest_framework import status
from rest_framework.response import Response
from rest_auth.registration.views import RegisterView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .serializers import JobOfferSerializer, JobTagsSerializer
from .models import User, JobOffer, JobTag
from .permissions import IsEmployer, IsOwner

class CustomRegisterView(RegisterView):
    queryset = User.objects.all()

class JobOffersViewSet(viewsets.ViewSet):
    serializer_class = JobOfferSerializer
    permission_classes = [IsEmployer&IsOwner]

    def list(self, request):
        jobs = JobOffer.objects.all()
        serializer = JobOfferSerializer(jobs, many = True)
        return Response(serializer.data)

    def create(self, request):
        serializer = JobOfferSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        queryset = JobOffer.objects.all()
        jobOffer = get_object_or_404(queryset, pk = pk)
        serializer = JobOfferSerializer(jobOffer)
        return Response(serializer.data)

    def update(self, request, pk = None):
        try:
            instance = JobOffer.objects.get(pk = pk)
            self.check_object_permissions(request, instance)
            serializer = JobOfferSerializer(instance = instance, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except JobOffer.DoesNotExist:
            serializer = JobOfferSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk = None):
        try:
            JobOffer.objects.get(pk = pk).delete()
            return Response(request.data, status = status.HTTP_200_OK)
        except JobOffer.DoesNotExist:
            content = {
                'status': 'Resource does not exist'
            }
            return Response(content, status = status.HTTP_404_NOT_FOUND)

class JobTagsViewSet(viewsets.ViewSet):
    serializer_class = JobTagsSerializer
    permission_classes = (IsEmployer, IsOwner)

    def list(self, request):
        tags = JobTag.objects.all()
        serializer = JobTagsSerializer(tags, many = True)
        return Response(serializer.data)

    def create(self, request):
        serializer = JobTagsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        queryset = JobTag.objects.all()
        tag = get_object_or_404(queryset, pk = pk)
        serializer = JobTagsSerializer(tag)
        return Response(serializer.data)

    def update(self, request, pk = None):
        try:
            instance = JobTag.objects.get(pk = pk)
            self.check_object_permissions(request, instance)
            serializer = JobTagsSerializer(instance = instance, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except JobTag.DoesNotExist:
            serializer = JobTagsSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk = None):
        try:
            JobTag.objects.get(pk = pk).delete()
            return Response(request.data, status = status.HTTP_200_OK)
        except JobTag.DoesNotExist:
            content = {
                'status': 'Resource does not exist'
            }
            return Response(content, status = status.HTTP_404_NOT_FOUND)
