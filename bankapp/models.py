from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

STATUS_CHOICE = [
    ('Blocked','BLOCK'),
    ('Normal','NORMAL')
]

class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    accountno = models.IntegerField()
    pin = models.IntegerField()

class Balance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

class Deposit(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    time = models.DateTimeField(default=datetime.now, blank=True)

class Withdrawal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    account = models.IntegerField()
    time = models.DateTimeField(default=datetime.now, blank=True)

class Transfer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    account = models.IntegerField()
    time = models.DateTimeField(default=datetime.now, blank=True)

class Account_Statuse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE,max_length=100,default='Normal')
