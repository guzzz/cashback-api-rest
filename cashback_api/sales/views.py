
import requests
from django.conf import settings

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Sale
from .serializers import SaleSerializer
from .filters import SaleFilter
from .filter_backends import SaleFilterBackend


class SaleModelViewSet(mixins.CreateModelMixin, 
				   mixins.RetrieveModelMixin, 
				   mixins.ListModelMixin,
				   viewsets.GenericViewSet):
	queryset = Sale.objects.none()
	serializer_class = SaleSerializer
	filter_class = SaleFilter
	filter_backends = (SaleFilterBackend,)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Sale.objects.all()


class AccumulatedFromOutsideApiViewSet(viewsets.ViewSet):
	queryset = Sale.objects.none()
	permission_classes = (IsAuthenticated,)

	def list(self, request):
		url = "https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf=12312312323"
		token = 'token '+settings.EXTERNAL_API_TOKEN
		response = requests.get(url, headers={'Authorization':token})
		settings.EXTERNAL_API_TOKEN
		if response.status_code == 200:
			return Response(response.json()['body'], status=status.HTTP_200_OK)
		else:
			return Response({'error': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)