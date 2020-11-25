from django.db.utils import IntegrityError
from django.test import TestCase

from cashback_api.users.models import CustomUser
from cashback_api.resellers.models import Reseller

from ..models import Sale


class SaleUnitTest(TestCase):
	@classmethod
	def setUpClass(cls):
		super(SaleUnitTest, cls).setUpClass()
		print('======================================================================')
		print('==> INITIALIZING Resellers UNIT Tests...')
		print('======================================================================')
		print('... CREATING initial Resellers ..............................')
		
		user_instance = CustomUser.objects.create(email="bale@email.com", password='cash1234')
		reseller_instance = Reseller.objects.create(cpf="210.159.040-92", full_name="Gareth Bale", user=user_instance)
		Sale.objects.create(code="VENDA1", value=132.50, date="2020-01-01", reseller=reseller_instance)

		print('----------------------------------------------------------------------')

	def test_create_existing_sale(self):
		print('==> Creating EXISTING sale')
		try:
			bale_reseller_instance = Reseller.objects.get(cpf="210.159.040-92")
			sale_1 = Sale.objects.create(code="VENDA1", value=132.50, date="2020-01-01", reseller=bale_reseller_instance)
			self.assertEqual(False, True)
		except IntegrityError as error:
			self.assertEqual(error.args[0], 'duplicate key value violates unique constraint "sales_sale_pkey"\nDETAIL:  Key (code)=(VENDA1) already exists.\n')
		print('----------------------------------------------------------------------')

	def test_create_new_sale(self):
		print('==> Creating NEW sale')
		try:
			bale_reseller_instance = Reseller.objects.get(cpf="210.159.040-92")
			sale_2 = Sale.objects.create(code="VENDA2", value=1732.58, date="2020-01-01", reseller=bale_reseller_instance)
			self.assertEqual(type(sale_2), Sale)
		except:
			self.assertEqual(False, True)
		print('----------------------------------------------------------------------')

	def test_sale_model(self):
		print('==> Testing MODEL')
		first_sale = Sale.objects.get(code="VENDA1")
		self.assertEqual(str(first_sale), "VENDA1")
		print('----------------------------------------------------------------------')
