# yieldapp/forms.py
from django import forms

class UploadCSVForm(forms.Form):
    process_type = forms.ChoiceField(choices=[
        ('filling', 'Filling'),
        ('inspection', 'Inspection'),
        ('assembly', 'Assembly'),
        ('blistering', 'Blistering'),
        ('packaging', 'Packaging'),
        ('handover', 'Handover to Warehouse'),
    ])
    file = forms.FileField()
