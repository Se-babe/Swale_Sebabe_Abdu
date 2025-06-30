from django.contrib import admin
from .models import Customer, Phone, RepairRecord

admin.site.register(Customer)
admin.site.register(Phone)
admin.site.register(RepairRecord)
