from django.db.utils import IntegrityError
from django.test import TestCase

from ..models import CustomUser


class UserUnitTest(TestCase):
	@classmethod
	def setUpClass(cls):
		super(UserUnitTest, cls).setUpClass()
		print('======================================================================')
		print('==> INITIALIZING Users UNIT Tests...')
		print('======================================================================')
		print('... CREATING initial Users ..............................')
		
		initial_user = CustomUser.objects.create(email="klose@email.com", password='cash1234')

		print('----------------------------------------------------------------------')

	def test_create_existing_user(self):
		print('==> Creating EXISTING user')
		try:
			klose_user = CustomUser.objects.create(email="klose@email.com", password='cash1234')
			self.assertEqual(False, True)
		except IntegrityError as error:
			self.assertEqual(error.args[0], 'duplicate key value violates unique constraint "users_customuser_email_key"\nDETAIL:  Key (email)=(klose@email.com) already exists.\n')
		print('----------------------------------------------------------------------')

	def test_create_new_user(self):
		print('==> Creating NEW user')
		try:
			zidane_user = CustomUser.objects.create(email="zidane@email.com", password='cash1234')
			self.assertEqual(type(zidane_user), CustomUser)
		except:
			self.assertEqual(False, True)
		print('----------------------------------------------------------------------')

	def test_custom_users_model(self):
		print('==> Testing MODEL')
		first_user = CustomUser.objects.get(email='klose@email.com')
		self.assertEqual(str(first_user), "klose@email.com")
		print('----------------------------------------------------------------------')
