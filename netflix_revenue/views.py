from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, CustomerForm
from .models import Customer
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Username or Password is wrong.')
    else:
        form = LoginForm()
    return render(request, 'netflix_revenue/login.html', {'form': form})

@login_required(login_url='/login/')
def home_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer.objects.create(
                user=request.user,
                name=form.cleaned_data['name'],
                service_type=form.cleaned_data['service_type'],
                payment_method=form.cleaned_data['payment_method'],
                duration=form.cleaned_data['duration'],
                total_payment=form.cleaned_data['total_payment']
            )
            messages.success(request, 'Data sent successfully!')
            return redirect('home')
    else:
        form = CustomerForm()

    customers = Customer.objects.all()
    total_customers = customers.count()
    total_by_service = customers.values('service_type').annotate(count=Count('id'))
    total_by_duration = customers.values('duration').annotate(count=Count('id'))
    total_transactions = customers.aggregate(Sum('total_payment'))['total_payment__sum'] or 0

    context = {
        'form': form,
        'total_customers': total_customers,
        'total_by_service': total_by_service,
        'total_by_duration': total_by_duration,
        'total_transactions': total_transactions,
    }

    return render(request, 'netflix_revenue/home.html', context)

@login_required(login_url='/login/')
def report_view(request):
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_by_service = customers.values('service_type').annotate(count=Count('id'))
    total_by_duration = customers.values('duration').annotate(count=Count('id'))
    total_transactions = customers.aggregate(Sum('total_payment'))['total_payment__sum'] or 0

    context = {
        'total_customers': total_customers,
        'total_by_service': total_by_service,
        'total_by_duration': total_by_duration,
        'total_transactions': total_transactions,
    }


    return render(request, 'netflix_revenue/report.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')




