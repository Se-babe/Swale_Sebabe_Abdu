from django import forms
from .models import RepairRecord

class RepairRecordForm(forms.ModelForm):
    class Meta:
        model = RepairRecord
        fields = ['issue_description', 'repair_status', 'repair_notes', 'repaired_on']
