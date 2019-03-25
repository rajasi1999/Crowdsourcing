from django import forms
from .models import User,Fundraiser,Donor,Amount


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget = forms.PasswordInput())
    ReEnter_Password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password','ReEnter_Password','aadhar_id')

class FundraiserForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ('organization_name','address_line_1','address_line_2','address_line_3','bank_name','bank_account_number','lobby_name')

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('organization_name','address_line_1','address_line_2','address_line_3')

class AmountForm(forms.ModelForm):
    class Meta:
        model = Amount
        fields = ('amount',)
