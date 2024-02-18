from django.db import models

# Create your models here.
class Sponsor(models.Model):
    full_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=80)
    website = models.CharField(max_length=100)
    message = models.TextField()

class Subscribe(models.Model):
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.email