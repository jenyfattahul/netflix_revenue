from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    SERVICE_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    DURATION_CHOICES = [
        ('1 month', '1 Month'),
        ('3 months', '3 Months'),
        ('1 year', '1 Year'),
    ]

    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('gopay', 'GoPay'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
