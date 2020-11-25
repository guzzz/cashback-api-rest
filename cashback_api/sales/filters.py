import django_filters

from .models import Sale


class SaleFilter(django_filters.FilterSet):
	date = django_filters.DateFromToRangeFilter()

	class Meta:
		model = Sale
		fields = (
			'status', 'date', 'cashback_percentage', 'reseller'
		)
