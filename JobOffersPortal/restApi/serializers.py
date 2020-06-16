from rest_framework import serializers
from restApi.models import User, JobTag, JobOffer, EmployerProfile
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import DefaultAccountAdapter

class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        email = data.get('email')
        name = data.get('name')
        surname = data.get('surname')
        phone_number = data.get('phone_number')
        isEmployer = data.get('isEmployer')
        if email:
            setattr(user, 'email', email)
        if name:
            setattr(user, 'name', name)
        if surname:
            setattr(user, 'surname', surname)
        if phone_number:
            setattr(user, 'phone_number', phone_number)
        if isEmployer:
            setattr(user, 'isEmployer', isEmployer)
        return super().save_user(request, user, form, commit = commit)

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required = True)
    password1 = serializers.CharField(write_only = True)
    name = serializers.CharField(required = True)
    surname = serializers.CharField(required = True)
    phone_number = serializers.CharField(required = True)
    isEmployer = serializers.BooleanField(required = False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'name': self.validated_data.get('name', ''),
            'surname': self.validated_data.get('surname', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'isEmployer': self.validated_data.get('isEmployer', 'false')
        }

    def save(self, request):
        user = super().save(request)
        user.save()
        return user


class CustomUserDetailsSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'surname', 'email', 'phone_number', 'isEmployer']
        read_only_fields = ('email',)


class JobTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTag
        fields = ['tag_id', 'name']


class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['profile_id', 'user_id', 'name', 'description', 'phone_number', 'email', 'address', 'website']


class JobOfferSerializer(serializers.ModelSerializer):
    jobTags = JobTagsSerializer(many = True, read_only = True)
    class Meta:
        model = JobOffer
        fields = ['employer_profile_id', 'job_adv_id', 'user_id', 'jobTags', 'name', 'description', 'expiration_date', 'salary']
