from rest_framework.test import APITestCase

from cashback_api.resellers.models import Reseller
from cashback_api.users.models import CustomUser

from ..models import Sale


class SaleTest(APITestCase):
	@classmethod
	def setUpClass(cls):
		super(SaleTest, cls).setUpClass()
		print('======================================================================')
		print('==> INITIALIZING Sales INTEGRATION Tests...')
		print('======================================================================')
		print('... CREATING initial Sales ..............................')
		
		user_1_instance = CustomUser.objects.create(email="messi@email.com")
		user_1_instance.set_password('cash1234')
		user_1_instance.save()
		user_2_instance = CustomUser.objects.create(email="ronaldo@email.com")
		user_2_instance.set_password('cash1234')
		user_2_instance.save()
		
		reseller_1 = Reseller.objects.create(cpf="866.314.750-31", full_name="Lionel Messi", user=user_1_instance)
		reseller_2 = Reseller.objects.create(cpf="153.509.460-56", full_name="Cristiano Ronaldo", user=user_2_instance)

		Sale.objects.create(code="VENDA1", value=132.50, date="2020-01-01", reseller=reseller_1)
		Sale.objects.create(code="VENDA2", value=1540.65, date="2020-01-01", reseller=reseller_1)
		Sale.objects.create(code="VENDA3", value=2999.99, date="2020-01-01", reseller=reseller_1)
		print('----------------------------------------------------------------------')

	def setUp(self):
		response = self.client.post('/api/token/', {"email":"messi@email.com","password":"cash1234"})
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

	def test_list_sales(self):
		print('==> LIST: [GET] /sales/')
		response = self.client.get('/sales/')
		self.assertEqual(response.status_code, 200)
		print('----------------------------------------------------------------------')

	def test_status_approved(self):
		print('==> CREATE: [POST] /sales/  (APPROVED)')
		response = self.client.post('/sales/', {"code":"VENDA4","value": 5000.30,"date":"2020-01-01","reseller":"153.509.460-56"})
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.json(), {'code': 'VENDA4', 'value': '5000.30', 'date': '2020-01-01', 'reseller': '153.509.460-56', 'status': 'Aprovado', 'cashback_percentage': 20, 'cashback_value': '1000.06'})
		print('----------------------------------------------------------------------')

	def test_status_awaiting_approval(self):
		print('==> CREATE: [POST] /sales/ (AWAITING APPROVAL)')
		response = self.client.post('/sales/', {'code': 'VENDA5', 'value': 1234.36, 'date': '2020-01-01', 'reseller': '866.314.750-31'})
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.json(), {'code': 'VENDA5', 'value': '1234.36', 'date': '2020-01-01', 'reseller': '866.314.750-31', 'status': 'Em validação', 'cashback_percentage': 15, 'cashback_value': '185.15'})
		print('----------------------------------------------------------------------')

	def test_api_integration(self):
		print('==> LIST: [GET] /accumulated-cashback-integration/')
		response = self.client.get('/accumulated-cashback-integration/')
		self.assertEqual(response.status_code, 200)
		print('----------------------------------------------------------------------')
