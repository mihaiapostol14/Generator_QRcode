from django import forms
from django.forms import ModelForm

from .models import QRCode


class QRCodeForm(ModelForm):  # README: QRCodeForm
    content = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter URL or text...',
        })
    )

    # New fields added from the Flask generator
    box_size = forms.IntegerField(
        min_value=1,
        initial=10,
        label='QR Code Size',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
        })
    )

    border = forms.IntegerField(
        min_value=0,
        initial=4,
        label='QR Code Border',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 0,
        })
    )

    fill_color = forms.CharField(
        max_length=20,
        initial='#000000',
        label='QR Code Color',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'color',
        })
    )

    back_color = forms.CharField(
        max_length=20,
        initial='#FFFFFF',
        label='Background Color',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'color',
        })
    )

    class Meta:
        model = QRCode
        fields = [
            'content',
            'box_size',
            'border',
            'fill_color',
            'back_color',
        ]