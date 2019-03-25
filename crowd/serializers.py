from rest_framework import serializers
from .models import User,Fundraiser,Donor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','aadhar_id')

class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundraiser
        fields = ('organization_name','bank_name','bank_account_number','lobby_name')
