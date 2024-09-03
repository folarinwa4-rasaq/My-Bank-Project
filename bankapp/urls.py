from django.urls import path
from bankapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('registeration/',views.registeration,name='registeration'),
    path('account/', views.account, name='account'),
    path('login/', views.login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('deposit/', views.deposit, name='deposit'),
    path('deposit-successful/', views.deposit_successful, name='deposit-successful'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('withdrawal-successful/', views.withdrawal_successful, name='withdrawal-successful'),
    path('transfer/', views.transfer, name='transfer'),
    path('transfer-successful/', views.transfer_successful, name='transfer-successful'),
]

