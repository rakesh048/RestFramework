from rest_framework import serializers
from django.contrib.auth.models import User
import re
from django.contrib.auth import login, authenticate

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=50)
    password = serializers.CharField(required=True, allow_blank=False, max_length=50)
    email = serializers.CharField(required=False, allow_blank=True, max_length=50)

    def validate_username(self, username):
        user = User.objects.filter(username=username).first()
        if user:
            raise serializers.ValidationError("User already registered!!")
        return username

    def validate_password(self, password):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password) and not re.findall('[A-Z]', password) and not len(re.findall('\d', password)) >= 8:
            raise serializers.ValidationError(("The password must contain at least one special character, one upper character and lenght should be {0}".format(8)))
        else:
            return password

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create_user(username=validated_data['username'],password=validated_data['password'])