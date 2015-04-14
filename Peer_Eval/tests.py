from django.test import TestCase
from django.test.html import HTMLParseError, parse_html
from django.test import Client

#Create your tests here.
class ViewTestCase(TestCase):
	#Meant to test the splash page link and return 200 or page found
	def testSplash(self):
		c = Client()
		response = c.post('/')
		self.assertEqual(response.status_code, 200)

	#Meant to test the login page link and return 200 or page found
	def testLogin(self):
		c = Client()
		response = c.post('/login/', {'username': 'jrf254', 'password': 'jrf254'})
		self.assertEqual(response.status_code, 200)

	#Meant to test the available page link and return 302 or page redirect as we are not loggeed in
	def testAvailable(self):
		c = Client()
		response = c.post('/available/')
		self.assertEqual(response.status_code, 302)

	#Meant to test the submitted page link and return 302 or page redirect as we are not loggeed in
	def testSubmitted(self):
		c = Client()
		response = c.post('/submitted/')
		self.assertEqual(response.status_code, 302)

	#Meant to test the admin page link and return 302 or page redirect as we are not loggeed in
	def testAdmin(self):
		c = Client()
		response = c.post('/admin/')
		self.assertEqual(response.status_code, 302)