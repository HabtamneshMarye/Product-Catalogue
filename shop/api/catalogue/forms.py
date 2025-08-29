from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["name","description","price","image","stock"]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:border-blue-500 focus:ring-1 focus:ring-blue-500'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:border-blue-500 focus:ring-1 focus:ring-blue-500'
            }),
            'description': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:border-blue-500 focus:ring-1 focus:ring-blue-500'
            }),
            'price': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:border-blue-500 focus:ring-1 focus:ring-blue-500'
            }),
            'stock': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:border-blue-500 focus:ring-1 focus:ring-blue-500'
            }),
        }

