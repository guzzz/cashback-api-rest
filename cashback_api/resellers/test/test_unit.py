from django.db.utils import IntegrityError
from django.test import TestCase

from cashback_api.users.models import CustomUser

from ..models import Reseller


class ResellerUnitTest(TestCase):
	@classmethod
	def setUpClass(cls):
		super(ResellerUnitTest, cls).setUpClass()
		print('======================================================================')
		print('==> INITIALIZING Resellers UNIT Tests...')
		print('======================================================================')
		print('... CREATING initial Resellers ..............................')
		
		user_instance = CustomUser.objects.create(email="imperador@email.com", password='cash1234')
		reseller = Reseller.objects.create(cpf="159.541.690-04", full_name="Adriano Imperador", user=user_instance)

		print('----------------------------------------------------------------------')

	def test_create_existing_reseller(self):
		print('==> Creating EXISTING reseller')
		try:
			imperador_instance = CustomUser.objects.get(email="imperador@email.com")
			imperador_reseller = Reseller.objects.create(cpf="159.541.690-04", full_name="Adriano Imperador", user=imperador_instance)
			self.assertEqual(False, True)
		except IntegrityError as error:
			self.assertEqual(error.args[0], 'duplicate key value violates unique constraint "resellers_reseller_pkey"\nDETAIL:  Key (cpf)=(159.541.690-04) already exists.\n')
		print('----------------------------------------------------------------------')

	def test_create_new_reseller(self):
		print('==> Creating NEW reseller')
		try:
			r10_user_instance = CustomUser.objects.create(email="gaucho@email.com", password='cash1234')
			r10_reseller = Reseller.objects.create(cpf="892.924.570-63", full_name="Ronaldinho Gaúcho", user=r10_user_instance)
			self.assertEqual(type(r10_reseller), Reseller)
		except:
			self.assertEqual(False, True)
		print('----------------------------------------------------------------------')

	def test_reseller_model(self):
		print('==> Testing MODEL')
		first_reseller = Reseller.objects.get(cpf='159.541.690-04')
		self.assertEqual(str(first_reseller), "159.541.690-04")
		print('----------------------------------------------------------------------')
