from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Customer

class LoginFlowTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='password123')

    def test_login_and_redirect_to_home(self):
        response = self.client.post(reverse('login'), {
            'username': 'tester',
            'password': 'password123',
        })
        self.assertRedirects(response, reverse('home'))

    def test_customer_form_submission(self):
        self.client.login(username='tester', password='password123')
        response = self.client.post(reverse('home'), {
            'name': 'Test Customer',
            'service_type': 'basic',
            'payment_method': 'credit_card',
            'duration': 'monthly',
            'total_payment': 100.00
        })
        self.assertEqual(Customer.objects.count(), 1)
        self.assertRedirects(response, reverse('home'))
