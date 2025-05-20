from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'wholesale_price': 'Wholesale Price',
            'retail_price': 'Retail Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder': 'e.g. 1', 'class': 'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g. iPhone', 'class': 'form-control'}),
            'sku': forms.TextInput(
                attrs={'placeholder': 'e.g. ABCD1234', 'class': 'form-control'}),
            'wholesale_price': forms.NumberInput(
                attrs={'placeholder': 'e.g. 899.99', 'class': 'form-control'}),
            'retail_price': forms.NumberInput(
                attrs={'placeholder': 'e.g. 999.99', 'class': 'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'placeholder': 'e.g. 10', 'class': 'form-control'}),
            'supplier': forms.TextInput(
                attrs={'placeholder': 'e.g. Apple', 'class': 'form-control'}),
        }