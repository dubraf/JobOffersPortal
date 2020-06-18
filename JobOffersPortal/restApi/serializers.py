from rest_framework import serializers
from restApi.models import User, JobTag, JobOffer, EmployerProfile, FavoriteJobOffer, CV
from rest_auth.registration.serializers import RegisterSerializer

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
    user_id = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = JobTag
        fields = ['tag_id', 'user_id', 'name']


class EmployerProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = EmployerProfile
        fields = ['profile_id', 'user_id', 'name', 'description', 'phone_number', 'email', 'address', 'website']


class JobOfferSerializer(serializers.ModelSerializer):
    jobTags = JobTagsSerializer(many = True)
    user_id = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = JobOffer
        fields = ['employer_profile_id', 'job_offer_id', 'user_id', 'jobTags', 'name', 'description', 'expiration_date', 'salary']

    def create(self, validated_data):
        job_tags_data = validated_data.pop('jobTags')
        job_offer = JobOffer.objects.create(**validated_data)
        for job_tag in job_tags_data:
            try:
                job_tag = JobTag.objects.get(name = job_tag['name'])
                job_offer.jobTags.add(job_tag)
            except JobTag.DoesNotExist:
                raise serializers.ValidationError({"detail": "Tag with given name doesn't exist"})
        return job_offer


class FavoriteJobOfferSerializer(serializers.ModelSerializer):
    job_offers = serializers.PrimaryKeyRelatedField(many = True, queryset = JobOffer.objects.all())
    user_id = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = FavoriteJobOffer
        fields = ['fav_job_offer_id', 'user_id', 'job_offers']

    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        if user_id.email != self.context['request'].user.email:
            raise serializers.ValidationError({"detail": "You can add favorite offers only to your account"})
        if user_id == FavoriteJobOffer.objects.filter(user_id = user_id):
            raise serializers.ValidationError({"detail": "Please update your existing favorite offers instead of creating new one"})
        job_offers_data = validated_data.pop('job_offers')
        favorite_job_offer = FavoriteJobOffer.objects.create(**validated_data)
        for job_offer_id in job_offers_data:
            try:
                job_offer = JobOffer.objects.get(job_offer_id = job_offer_id.pk)
                favorite_job_offer.job_offers.add(job_offer)
            except JobOffer.DoesNotExist:
                raise serializers.ValidationError({"detail": "Job offer with given id doesn't exist"})
        return favorite_job_offer

class CVSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = CV
        fields = ['cv_id', 'user_id', 'file']

