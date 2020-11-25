from rest_framework import serializers

from .models import Sale
from .services import check_cpf, calculate_cashback
from .choices import ACTIVATION_CHOICES_TRANSLATION


class SaleSerializer(serializers.ModelSerializer):
	status = serializers.SerializerMethodField()
	cashback_percentage = serializers.ReadOnlyField()
	cashback_value = serializers.ReadOnlyField()

	class Meta:
		model = Sale
		fields = ('code','value','date','reseller','status','cashback_percentage','cashback_value')

	def get_status(self, obj):
		return dict(ACTIVATION_CHOICES_TRANSLATION)[obj.status]


	def create(self, validated_data):
		if check_cpf(validated_data['reseller'].pk):
			validated_data['status'] = 'approved'
		
		cashback_percentage, cashback_value = calculate_cashback(validated_data['value'])
		validated_data['cashback_percentage'] = cashback_percentage
		validated_data['cashback_value'] = cashback_value
		return Sale.objects.create(**validated_data)