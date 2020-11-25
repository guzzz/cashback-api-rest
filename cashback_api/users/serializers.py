from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(required=True, write_only=True)

	class Meta:
		model = CustomUser
		fields = ('email','password')
