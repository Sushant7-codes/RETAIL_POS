from django.shortcuts import render,redirect

# Create your views here.

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/register.html')

def home_redirect(request):
    return redirect('/accounts/login/')

