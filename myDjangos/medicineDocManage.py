from django import forms

from .models import MedicineDocument, Medicine


class MedicineDocForm(forms.ModelForm):
    class Meta:
        model = MedicineDocument
        fields = ['medicine_document_name']
        labels = {'medicine_document_name': ''}
        widgets = {'medicine_document_name': forms.Textarea(attrs={'cols': 80})}


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['medicine_name']
        labels = {'medicine_name': '药品名称'}
