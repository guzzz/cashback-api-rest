import json
from rest_framework.test import APITestCase

from cashback_api.users.models import CustomUser

from ..models import Reseller


class ResellerTest(APITestCase):
	@classmethod
	def setUpClass(cls):
		super(ResellerTest, cls).setUpClass()
		print('======================================================================')
		print('==> INITIALIZING Resellers INTEGRATION Tests...')
		print('======================================================================')
		print('... CREATING initial Resellers ..............................')
		
		user_1_instance = CustomUser.objects.create(email="drogba@email.com")
		user_1_instance.set_password('cash1234')
		user_1_instance.save()
		user_2_instance = CustomUser.objects.create(email="ibra@email.com")
		user_2_instance.set_password('cash1234')
		user_2_instance.save()

		reseller_1 = Reseller.objects.create(cpf="787.726.170-55", full_name="Didier Drogba", user=user_1_instance)
		reseller_2 = Reseller.objects.create(cpf="049.489.600-04", full_name="Zlatan Ibrahimović", user=user_2_instance)

		print('----------------------------------------------------------------------')

	def setUp(self):
		response = self.client.post('/api/token/', {"email":"drogba@email.com","password":"cash1234"})
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

	def test_list_resellers(self):
		print('==> LIST: [GET] /resellers/')
		response = self.client.get('/resellers/')
		self.assertEqual(response.status_code, 200)
		print('----------------------------------------------------------------------')

	def test_create_reseller(self):
		print('==> CREATE: [POST] /resellers/')
		data = {"cpf":"770.434.330-02","full_name": "Michael Owen",'user':{ "email": "owen@email.com", "password": "cash1234"}}
		response = self.client.post('/resellers/', data=json.dumps(data), content_type="application/json")
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.json(), {"cpf":"770.434.330-02","full_name":"Michael Owen","user":{"email": "owen@email.com"}})
		print('----------------------------------------------------------------------')
