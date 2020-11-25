
from decimal import Decimal


def check_cpf(cpf):
	if cpf == '153.509.460-56':
		return True
	else:
		return False


def calculate_cashback(value):
	if value <= 1000:
		return 10, "{:.2f}".format(value*Decimal(0.10))
	elif 1000 < value < 1500:
		return 15, "{:.2f}".format(value*Decimal(0.15))
	else: 
		return 20, "{:.2f}".format(value*Decimal(0.20))