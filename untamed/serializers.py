from rest_framework import serializers
from urllib3 import Retry
from .models import Event, Profile, User
from django.contrib.auth import login


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__' 
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = '__all__'
        
class UserCreateAccount(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email','username', 'password','password2','is_host','is_attendee']
        
    def save(self):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            is_host = self.validated_data['is_host'],
            is_attendee = self.validated_data['is_attendee']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({"password":'Password must match.'})
        account.set_password(password)
        account.save()
        return account
    