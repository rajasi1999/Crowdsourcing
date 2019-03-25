from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_fundraiser = models.BooleanField(default = False)
    is_donor = models.BooleanField(default = False)
    aadhar_id = models.CharField(max_length=12, default="0", unique = True)
    #aadharcard_upload = models.FileField(upload_to='media/')

class Fundraiser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    organization_name = models.CharField(max_length =128 ,blank = True, unique = True)
    address_line_1 = models.CharField(max_length = 32)
    address_line_2 = models.CharField(max_length = 32)
    address_line_3 = models.CharField(max_length = 32)
    lobby_name = models.CharField(max_length = 32, unique = True)
    bank_name = models.CharField(max_length = 32)
    bank_account_number = models.IntegerField()
    def is_fundraiser(self):
        self.user.is_fundraiser = True

class Donor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    organization_name = models.CharField(max_length =128 ,blank = True, unique = True)
    address_line_1 = models.CharField(max_length = 32)
    address_line_2 = models.CharField(max_length = 32)
    address_line_3 = models.CharField(max_length = 32)

    def is_investor(self):
        self.user.is_donor = True
class Amount(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    amount = models.IntegerField()
