from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Phones
    path('phones/', views.PhoneListView.as_view(), name='phone_list'),
    path('phones/<int:pk>/', views.PhoneDetailView.as_view(), name='phone_detail'),
    path('phones/add/', views.PhoneCreateView.as_view(), name='phone_add'),

    # Customers
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),

    # Repair Records
    path('phones/<int:phone_id>/repairs/add/', views.add_repair_record, name='add_repair'),
]
