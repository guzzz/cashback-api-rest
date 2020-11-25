from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

from .choices import ACTIVATION_CHOICES


class Sale(models.Model):
	code = models.CharField(primary_key=True, max_length=50)
	status = models.CharField(blank=True, default='awaiting_approval', max_length=20, choices=ACTIVATION_CHOICES)
	value = models.DecimalField(
		decimal_places=2,
		max_digits=20,
	)
	date = models.DateField(null=False)
	cashback_percentage = models.DecimalField(
		blank=True,
		null=True,
		decimal_places=0,
		max_digits=2,)
	cashback_value = models.DecimalField(
		blank=True,
		null=True,
		decimal_places=2,
		max_digits=20,
	)
	reseller = models.ForeignKey(
		to='resellers.Reseller',
		related_name='%(class)s',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.code


@receiver(post_save, sender=Sale)
def check_cashback(sender, instance=None, created=False, **kwargs):
	if created and (not instance.cashback_percentage or not instance.cashback_value):
		from .services import calculate_cashback
		cashback_percentage, cashback_value = calculate_cashback(Decimal(instance.value))
		instance.cashback_percentage = cashback_percentage
		instance.cashback_value = cashback_value
		instance.save()
