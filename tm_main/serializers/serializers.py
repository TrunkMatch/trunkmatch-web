from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from tm_main.models import Profile


class RegistrationSerializer(serializers.ModelSerializer, RegisterSerializer):
    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', '')
        }

    class Meta:
        model = Profile
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')
