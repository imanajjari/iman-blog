from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def login_view(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('/')


    return render(request, 'accounts/login.html', {})

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def singup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'accounts/singup.html', context)
    else:
        return redirect('/')