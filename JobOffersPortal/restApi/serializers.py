from rest_framework import serializers
from restApi.models import User
from rest_auth.registration.serializers import  RegisterSerializer

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

class CustomUserDetailsSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'phone_number', 'isEmployer']
        read_only_fields = ('email',)