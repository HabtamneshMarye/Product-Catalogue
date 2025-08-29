from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def list_products(request):
    products = Product.objects.all()
    return render(request, "catalogue/products.html", {"products": products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "catalogue/product_details.html", {"product": product})


@login_required(login_url="/accounts/login/")
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_products")
    else:
        form = ProductForm()
    return render(request, "catalogue/create_product.html", {"form": form})
