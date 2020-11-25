from django.contrib import admin

from .models import Reseller
from .forms import ResellerForm


@admin.register(Reseller)
class ResellerAdmin(admin.ModelAdmin):
	form = ResellerForm

