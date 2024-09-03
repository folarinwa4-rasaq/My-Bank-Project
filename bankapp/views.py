from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Account,Account_Statuse,Balance,Withdrawal,Deposit,Transfer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='login')
def home(request):
    user = request.user
    p = Account.objects.get(user=request.user)
    bal = Balance.objects.order_by('user').last()
    state = Account_Statuse.objects.get(user=request.user)   
    if state.status == 'Blocked':
        messages.warning(request,'Your Account Has Been Blocked')
    return render(request, 'home.html',{'user':user,'p':p,'bal':bal})

@login_required(login_url='login')
def about(request):
    state = Account_Statuse.objects.get(user=request.user)   
    if state.status == 'Blocked':
        messages.warning(request,'Your Account Has Been Blocked')
    return render(request, 'about.html')

def registeration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already used')
                return redirect('registeration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('registeration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('account')
        else:
            messages.info(request, 'password not the same')
            return redirect('registeration')
    else:
        return render(request, 'registeration.html')

def account(request):
    if request.method == 'POST':
        name = request.POST['name']
        account = request.POST['acct']
        pin = request.POST['pin']
        pin2 = request.POST['pin2']

        if pin == pin2:
            user = User.objects.get(username=name)
            if Account.objects.filter(accountno=account).exists():
                messages.warning(request, 'Mobile Number Already Used')
                return redirect('account')
            elif len('pin' and 'pin2') > 4:
                messages.warning(request, 'Pin Must Be Four Character')
                return redirect('account')
            else:
                Ac = Account(user=user, accountno=account, pin=pin)
                Ac.save()
                A = Account.objects.get(user=user)
                status = Account_Statuse(user=user,account=A,status='Normal')
                bal = Balance(user=user)
                status.save()
                bal.save()
                return redirect('login')
        else:
            messages.warning(request, 'Pin Didn`t match')
            return redirect('account')
    else:
        return render(request, 'account.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def deposit(request):
    user = request.user
    state = Account_Statuse.objects.get(user=request.user)   
    if state.status == 'Blocked':
        messages.warning(request,'Your Account Has Been Blocked')
    if request.method == 'POST':
        account = request.POST['acct']
        amount = int(request.POST['amount'])
        pin = request.POST['pin']
        deposit = Balance.objects.filter(user=request.user)
        #for b in deposit:
        tot_bal = amount
        info = Deposit(amount=amount,user=user)
        info.save()
        bal = Balance(amount=tot_bal,user=user)
        bal.save()
        return redirect('deposit-successful')
    else:
        return render(request, 'deposit.html')

@login_required(login_url='login')
def deposit_successful(request):
    account = Account.objects.filter(user=request.user)
    deposit = Deposit.objects.order_by('user').last()
    return render(request, 'deposit-successful.html',{'account':account,'deposit':deposit})

@login_required(login_url='login')
def withdraw(request):
    user = request.user
    state = Account_Statuse.objects.get(user=request.user)   
    if state.status == 'Blocked':
        messages.warning(request,'Your Account Has Been Blocked')
    if request.method == 'POST':
        account = request.POST['acct']
        amount = int(request.POST['amount'])
        pin = request.POST['pin']
        old_bal = Balance.objects.filter(user=request.user)
        for b in old_bal:
            t = b.amount
        if amount <= t:
            for b in old_bal:
                bal = b.amount - amount
            details = Withdrawal(user=user,account=account,amount=amount)
            details.save()
            tot_bal = Balance(user=user,amount=bal)
            tot_bal.save()
        else:
            messages.warning(request, 'Insufficient Balance')
            return redirect('withdraw')
        return redirect('withdrawal-successful')
    else:
        return render(request, 'withdraw.html')

@login_required(login_url='login')
def withdrawal_successful(request):
    account = Account.objects.get(user=request.user)
    withdraw = Withdrawal.objects.order_by('user').last()
    return render(request, 'withdrawal-successful.html',{'account':account,'withdraw': withdraw})

@login_required(login_url='login')
def transfer(request):
    user = request.user
    state = Account_Statuse.objects.get(user=request.user)   
    if state.status == 'Blocked':
        messages.warning(request,'Your Account Has Been Blocked')
    if request.method == 'POST':
        account = request.POST['acct']
        amount = int(request.POST['amount'])
        pin = request.POST['pin']
        old_bal = Balance.objects.filter(user=request.user)
        for b in old_bal:
            t = b.amount
        if amount <= t:
            for b in old_bal:
                bal = b.amount - amount
            details = Balance(user=user,amount=bal)
            details.save()
            trans = Transfer(user=user,amount=amount,account=account)
            trans.save()
        else:
            messages.warning(request, 'Insufficient Balance')
            return redirect('withdraw')
        return redirect('transfer-successful')
    return render(request, 'transfer.html')

@login_required(login_url='login')
def transfer_successful(request):
    user=request.user
    transfer = Transfer.objects.order_by('user').last()
    account = Account.objects.get(user=request.user)
    return render(request, 'transfer-successful.html',{'account':account,'transfer':transfer,'user':user})

