from django.shortcuts import render

# Create your views here.

def sales_home_view(request):
    return render(request, 'sales/home.html')