from django import forms
from django.forms import ModelForm

from .models import QRCode

class QRCodeForm(ModelForm):
    content = forms.CharField(
        max_length=225,
        label='',  
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter URL or text...',
        })
    )

    class Meta:
        model = QRCode
        fields = ['content']
        