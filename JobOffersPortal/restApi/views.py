from rest_framework.parsers import MultiPartParser
from rest_auth.registration.views import RegisterView
from rest_framework import viewsets, mixins
from .serializers import JobOfferSerializer, JobTagsSerializer, EmployerProfileSerializer, FavoriteJobOfferSerializer, \
    CVSerializer
from .models import User, JobOffer, JobTag, EmployerProfile, FavoriteJobOffer, CV
from .permissions import IsEmployer, IsStandardUser, IsOwner

class CustomRegisterView(RegisterView):
    queryset = User.objects.all()

class JobOffersViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    permission_classes = [IsEmployer & IsOwner]

    def get_serializer_context(self):
        context = super(JobOffersViewSet, self).get_serializer_context()
        return context

class JobTagsViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = JobTag.objects.all()
    serializer_class = JobTagsSerializer
    permission_classes = (IsEmployer, IsOwner)

class EmployerProfileViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsEmployer, IsOwner]

class FavoriteJobOffersViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    queryset = FavoriteJobOffer.objects.all()
    serializer_class = FavoriteJobOfferSerializer
    permission_classes = [IsStandardUser, IsOwner]

class CVViewSet(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    queryset = CV.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = CVSerializer
    permission_classes = [IsStandardUser, IsOwner]

    def get_queryset(self):
        user_cvs = CV.objects.filter(user_id = self.request.user.user_id)
        return user_cvs