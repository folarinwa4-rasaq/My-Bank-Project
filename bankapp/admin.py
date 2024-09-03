from django.contrib import admin
from .models import Account,Balance,Deposit,Withdrawal,Transfer,Account_Statuse

# Register your models here.
admin.site.register(Account)
admin.site.register(Balance)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
admin.site.register(Transfer)
admin.site.register(Account_Statuse)

