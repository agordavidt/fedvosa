from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('faq', views.faq, name='faq'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pay', views.pay, name='pay'),
]