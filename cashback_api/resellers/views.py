from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Reseller
from .serializers import ResellerSerializer


class ResellerModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	queryset = Reseller.objects.all()
	serializer_class = ResellerSerializer
	permission_classes = (IsAuthenticated,)
