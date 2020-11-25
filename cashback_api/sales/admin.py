from django.contrib import admin

from .models import Sale
from .services import check_cpf


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):

	def save_model(self, request, obj, form, change):
		super().save_model(
			request, obj, form, change
		)
		if not change and check_cpf(obj.reseller.pk):
			obj.status = 'approved'
			obj.save()