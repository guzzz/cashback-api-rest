
from rest_framework import serializers
from django.contrib.auth.base_user import BaseUserManager
from localflavor.br.forms import BRCPFField
from brazilnum.cpf import validate_cpf

from cashback_api.users.models import CustomUser
from cashback_api.users.serializers import CustomUserSerializer

from .models import Reseller


class ResellerSerializer(serializers.ModelSerializer):
	user = CustomUserSerializer()

	class Meta:
		model = Reseller
		fields = ('cpf','full_name','user')
	
	def validate_cpf(self, cpf):
		if not validate_cpf(cpf):
			raise serializers.ValidationError('invalid cpf.')
		return cpf

	def create(self, validated_data):
		serializer_user = validated_data.pop('user')
		serializer_email = serializer_user.pop('email')
		serializer_password = serializer_user.pop('password')

		email = BaseUserManager.normalize_email(serializer_email)
		user = CustomUser.objects.create(email=email)
		user.set_password(serializer_password)
		user.save()
		validated_data['user'] = user
		return Reseller.objects.create(**validated_data)
