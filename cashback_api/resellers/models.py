from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from cashback_api.users.models import CustomUser


class Reseller(models.Model):
	cpf = models.CharField(primary_key=True, max_length=15)
	full_name = models.CharField(max_length=150, verbose_name=_('Nome Completo'))
	user = models.OneToOneField(
		to=settings.AUTH_USER_MODEL,
		verbose_name=_('user'),
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.cpf