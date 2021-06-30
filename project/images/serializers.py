from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import FileField
from rest_framework.serializers import ModelSerializer

from .models import Storage

class StorageSerializer(ModelSerializer):
    class Meta:
        model = Storage
        fields = ['id', 'fileName', 'path','file', 'owner']


User = get_user_model()


class LoginSerializers(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        username = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data



class UploadSerializer(serializers.Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']