from logging import exception

import google.genai.errors
from django.shortcuts import render, redirect
from google import genai

# Create your views here.
from .forms import ProductForm
from .models import Product

# CRUD = Create, Read, Update, Delete
# Home View
def home_view(request):
    return render(request, 'todo/home.html')
# Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'todo/product_form.html', {'form': form})
# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'todo/product_list.html', {'products': products})
# Update View
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'todo/product_form.html', {'form': form})
# Delete View
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'todo/product_delete.html', {'product': product})
# Analysis View
def ai_analysis_view(request):
    products = Product.objects.all()
    product_string = []
    for product in products:
        product_string.append(f"{product.name}, {product.sku}, {product.wholesale_price}, {product.retail_price}, {product.quantity}, {product.supplier}")
    product_table = "\n".join(product_string)
    text_input = """The following table represents the inventory of store with each row containing the name of a product, 
        its SKU, wholesale price, retail price, quantity, and supplier, all seperated by a comma. Each row is a single product.
        Analysis the data and provide a summary of the inventory, along with recommendations on pricing, and a prediction
        on how the store will perform in the future.
        """
    text_input += product_table
    try:
        client = genai.Client(api_key="INSERT API KEY HERE")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=text_input,
        )
        output = response.text
    except Exception as e:
        output = "Error: " + str(e)
    return render(request, 'todo/ai_analysis.html', {'output': output})
