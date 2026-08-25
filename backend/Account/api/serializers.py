from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import User
from django.contrib.auth import authenticate # Django's built-in password checker

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.Charfield(write_only=True, min_lenght=8)
    
    class Meta:
        model = User
        fields = ('username','email','password')
        
    def create(self, validated_data):
        validated_data['passoword'] = make_password(validated_data['password']) #hash the password
        return User.objects.create(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        try:
            user = User.objects.get(email=email)
            username = user.username
        except:
            raise serializers.ValidationError("Invalid credentials")
        
        user = authenticate(username=username, password=password)
        
        if not user:
            raise serializers.ValidationError("invalid credentials")
        
        attrs['user'] = user
        return attrs
    
        
    