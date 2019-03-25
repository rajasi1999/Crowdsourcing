from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('register/donor', views.register_donor, name ='donor_register'),
    path('register/fundraiser', views.register_fundraiser, name ='fundraiser_register'),
    path('login/',views.user_login, name = 'user_login'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path('activate/<str:uidb64>/<str:token>',views.activate, name = 'activate'),
    path('payment/',views.payment,name = 'payment'),
    path('browse/',views.browsefiles, name = 'browse'),
    path('work/',views.howitworks,name = 'work'),
]
