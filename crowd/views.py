from django.shortcuts import render, redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from rest_framework import viewsets, permissions, status, views
import requests
import json
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from rest_framework import viewsets
from .models import User,Fundraiser,Donor
from .forms import (
                    UserForm,
                    FundraiserForm,
                    DonorForm,
                    AmountForm
                    )
from .serializers import UserSerializer,FundraiserSerializer


# Create your views here.

def index(request):
    return render(request,'crowd/home.html')

def register_donor(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        donor_form = DonorForm(data=request.POST)
        password1 = request.POST['password']
        password2 = request.POST['ReEnter_Password']
        if password1 == password2:
            if user_form.is_valid() and donor_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                donor = donor_form.save(commit=False)
                donor.user = user
                donor.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                print(user.pk)
                message = render_to_string('crowd/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uidb64':user.pk,
                'token':account_activation_token.make_token(user),
            })
                to_email = user_form.cleaned_data.get('email')
                email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
                email.send()
            else:
                print(user_form.errors, donor_form.errors)
    else:
        user_form = UserForm()
        donor_form = DonorForm()

    return render(request,'crowd/signup.html',{'user_form':user_form,'donor_form':donor_form})


def register_fundraiser(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        fundraiser_form = FundraiserForm(data=request.POST)
        password1 = request.POST['password']
        password2 = request.POST['ReEnter_Password']
        if password1 == password2:
            if user_form.is_valid() and fundraiser_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.is_active = False
                user.save()
                fundraiser = fundraiser_form.save(commit=False)
                fundraiser.user = user
                fundraiser.save()
                print('Please confirm your email address to complete the registration  ----- 1')
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('crowd/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uidb64':user.pk,
                'token':account_activation_token.make_token(user),
            })
                to_email = user_form.cleaned_data.get('email')
                email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
                email.send()


            else:
                print(user_form.errors, fundraiser_form.errors)
    else:
        user_form = UserForm()
        fundraiser_form = FundraiserForm()

    return render(request,'crowd/signup_fundraiser.html',{'user_form':user_form,'fundraiser_form':fundraiser_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username ,password = password)
        login_user = False
        if user:
            if user.is_active:
                login(request,user)
                return render(request,'crowd/home.html')
            else:
                return HttpResponse("Account Not active")
        else:
            login_user = True
            return render(request,'crowd/login.html',{'login_user':login_user})

    else:
        return render(request,'crowd/login.html',{})

# For generating activation link
def activate(request, uidb64, token):
    try:
        user = User.objects.get(pk=uidb64)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return render(request,'crowd/email_verified.html')
    else:
        return render(request,'crowd/not_verified.html')


class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer

class FundViewSet(viewsets.ModelViewSet):
    queryset = Fundraiser.objects.all()
    serializer_class = FundraiserSerializer

def payment(request):
    return render(request,'payment/pay.html')

def browsefiles(request):
    return render(request,'crowd/browsing_fundraisers.html')

def howitworks(request):
    return render(request,'crowd/howitworks.html')
