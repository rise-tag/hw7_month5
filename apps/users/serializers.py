from rest_framework import serializers
import re
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'password', 'confirm_password']

    def create(self, validated_data): 
        user = User.objects.create(
            username=validated_data['username'], 
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Пароли не совпадают"})
        
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password': "Минимум 8 символов"})
        
        if not re.match(r'^\+996\d{9}$', attrs['phone_number']):
            raise serializers.ValidationError({'phone_number': "Номер телефона должен быть в формате +996123456789."})
        
        return attrs