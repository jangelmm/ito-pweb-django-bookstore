from django.views.generic import ListView, DetailView
from .models import Product

class ProductList(ListView):
    model = Product
    # Django automáticamente busca: products/product_list.html

class ProductDetail(DetailView):
    model = Product  
    # Django automáticamente busca: products/product_detail.html