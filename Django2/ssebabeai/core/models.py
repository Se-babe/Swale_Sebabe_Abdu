from django.db import models

# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Phone Model
class Phone(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    imei = models.CharField(max_length=20, unique=True)
    received_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.imei}"


# Repair Record Model
class RepairRecord(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    issue_description = models.TextField()
    repair_status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ], default='Pending')
    repair_notes = models.TextField(blank=True)
    repaired_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.phone} - {self.repair_status}"
