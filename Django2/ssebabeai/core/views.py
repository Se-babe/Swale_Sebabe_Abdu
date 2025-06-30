from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Phone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Phone, RepairRecord
from .forms import RepairRecordForm
from django.contrib.auth.mixins import LoginRequiredMixin

    


# Homepage
def home(request):
    return render(request, 'core/home.html')

# Phone List View
class PhoneListView(ListView):
    model = Phone
    template_name = 'core/phone_list.html'
    context_object_name = 'phones'

# Phone Detail View
class PhoneDetailView(DetailView):
    model = Phone
    template_name = 'core/phone_detail.html'
    context_object_name = 'phone'

# Phone Create View
class PhoneCreateView(CreateView):
    model = Phone
    fields = ['customer', 'brand', 'model', 'imei']
    template_name = 'core/phone_form.html'
    success_url = reverse_lazy('phone_list')



# --- CUSTOMER VIEWS ---

class CustomerListView(ListView):
    model = Customer
    template_name = 'core/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'core/customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'core/customer_form.html'
    success_url = reverse_lazy('customer_list')

# --- REPAIR RECORD VIEW ---

def add_repair_record(request, phone_id):
    phone = get_object_or_404(Phone, id=phone_id)
    if request.method == 'POST':
        form = RepairRecordForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.phone = phone
            form.save()
            return redirect('phone_detail', pk=phone_id)
    else:
        form = RepairRecordForm()
    return render(request, 'core/repair_form.html', {'form': form, 'phone': phone})
