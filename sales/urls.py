from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_home_view, name='sales_home'),
]