# Resumen del Proyecto Django: bookstore-project

Ruta base: `/media/Files/Documentos/Programacion/Python/bookstore-project`

## Estructura del proyecto
```text
bookstore-project
└── bookstore
    ├── bookstore
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── products
    │   ├── management
    │   │   └── commands
    │   │       └── load_sample_products.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_alter_product_options_product_created_at_and_more.py
    │   │   └── __init__.py
    │   ├── templates
    │   │   └── products
    │   │       ├── product_confirm_delete.html
    │   │       ├── product_detail.html
    │   │       ├── product_form.html
    │   │       └── product_list.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── static
    │   ├── css
    │   │   └── style.css
    │   ├── images
    │   └── js
    ├── db.sqlite3
    └── manage.py
```

## Contenido de Archivos

### `bookstore/manage.py`
```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

### `bookstore/bookstore/asgi.py`
```python
"""
ASGI config for bookstore project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

application = get_asgi_application()
```

### `bookstore/bookstore/settings.py`
```python
"""
Django settings for bookstore project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-wt85a_b70vtnns5pvr-ws!y+w==d31&vi3qqv$l=(13)#22tp#'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # ← ¡IMPORTANTE!
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True

# Configuración para archivos estaticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Para desarrollo
]

# Configuracion para archivos de tipo media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'```

### `bookstore/bookstore/urls.py`
```python
"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('product/new/', ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)```

### `bookstore/bookstore/wsgi.py`
```python
"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

application = get_wsgi_application()
```

### `bookstore/bookstore/__init__.py`
```python
# (Archivo vacío)
```

### `bookstore/products/admin.py`
```python
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']```

### `bookstore/products/apps.py`
```python
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
```

### `bookstore/products/forms.py`
```python
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Título del producto',
                'minlength': '3',  # ← Validación HTML5
                'maxlength': '200', # ← Validación HTML5
                'required': 'true', # ← Validación HTML5
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-field',
                'rows': 4,
                'placeholder': 'Descripción del producto',
                'minlength': '10',  # ← Mínimo 10 caracteres
                'required': 'true',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-field',
                'step': '0.01',
                'min': '0.01',      # ← Mínimo $0.01
                'max': '999999.99', # ← Máximo según max_digits=8
                'placeholder': '0.00',
                'required': 'true',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-field',
                'accept': 'image/*', # ← Solo aceptar imágenes
            })
        }
    
    # Validación del servidor (siempre necesaria)
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title.strip()) < 3:
            raise forms.ValidationError("El título debe tener al menos 3 caracteres")
        return title
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor a 0")
        return price```

### `bookstore/products/models.py`
```python
from django.db import models
from django.core.validators import MinValueValidator  # ← Agregar este import
from decimal import Decimal

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.FileField(
        upload_to='products/', 
        blank=True, 
        null=True,
        verbose_name="Archivo adjunto"
    )
    price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        verbose_name="Precio",
        validators=[MinValueValidator(Decimal('0.01'))]  # ← Corregido
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"```

### `bookstore/products/tests.py`
```python
from django.test import TestCase

# Create your tests here.
```

### `bookstore/products/views.py`
```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm  # ← Vamos a crear esto

class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')```

### `bookstore/products/__init__.py`
```python
# (Archivo vacío)
```

### `bookstore/products/management/commands/load_sample_products.py`
```python
from django.core.management.base import BaseCommand
from products.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Carga productos de ejemplo (equivalente a Rails seeds)'

    def handle(self, *args, **options):
        sample_products = [
            {
                'title': 'El Quijote de la Mancha',
                'description': 'La obra maestra de Miguel de Cervantes que narra las aventuras de Alonso Quijano.',
                'price': Decimal('25.99'),
            },
            {
                'title': 'Cien Años de Soledad',
                'description': 'Novela del realismo mágico por Gabriel García Márquez que cuenta la historia de la familia Buendía.',
                'price': Decimal('22.50'),
            },
            {
                'title': '1984',
                'description': 'Distopía clásica de George Orwell sobre un régimen totalitario y la vigilancia masiva.',
                'price': Decimal('18.75'),
            },
        ]

        for product_data in sample_products:
            product, created = Product.objects.get_or_create(
                title=product_data['title'],
                defaults=product_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f' Producto creado: {product.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f' Producto ya existe: {product.title}')
                )```

### `bookstore/products/migrations/__init__.py`
```python
# (Archivo vacío)
```

### `bookstore/products/templates/products/product_confirm_delete.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eliminar Producto - Bookstore</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="header">
        <div class="container">
            <h1>Eliminar Producto</h1>
        </div>
    </div>

    <div class="container">
        <div class="delete-confirmation">
            <h2>¿Estás seguro de que quieres eliminar este producto?</h2>
            <div class="product-preview">
                <h3>{{ object.title }}</h3>
                <p>{{ object.description|truncatewords:20 }}</p>
                <p class="price">${{ object.price }}</p>
            </div>
            
            <form method="post" class="delete-form">
                {% csrf_token %}
                <div class="form-actions">
                    <button type="submit" class="btn btn-danger">Sí, eliminar</button>
                    <a href="{% url 'product_list' %}" class="btn btn-secondary">Cancelar</a>
                </div>
            </form>
        </div>
    </div>
</body>
</html>```

### `bookstore/products/templates/products/product_detail.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ object.title }} - Bookstore</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="header">
        <div class="container">
            <h1>Detalles del Producto</h1>
        </div>
    </div>

    <div class="container">
        <div class="product-detail">
            {% if object.image %}
            <img src="{{ object.image.url }}" alt="{{ object.title }}" class="detail-image">
            {% endif %}
            
            <h2>{{ object.title }}</h2>
            <p><strong>Descripción:</strong></p>
            <p>{{ object.description }}</p>
            
            <p class="product-price">Precio: ${{ object.price }}</p>
            
            <div style="margin-top: 2rem;">
                <a href="{% url 'product_list' %}" class="btn btn-secondary">
                    ← Volver a la lista
                </a>
            </div>
        </div>
    </div>
</body>
</html>```

### `bookstore/products/templates/products/product_form.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if form.instance.pk %}Editar{% else %}Crear{% endif %} Producto - Bookstore</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="header">
        <div class="container">
            <h1>{% if form.instance.pk %} Editar{% else %}  Crear{% endif %} Producto</h1>
        </div>
    </div>

    <div class="container">
        <div class="form-container">
            <!-- 
                IMPORTANTE: novalidate="false" permite validación HTML5 
                El navegador mostrará mensajes automáticamente
            -->
            <form method="post" enctype="multipart/form-data" class="product-form" novalidate="false">
                {% csrf_token %}
                
                {% for field in form %}
                <div class="form-group">
                    <label for="{{ field.id_for_label }}">
                        {{ field.label }}
                        {% if field.field.required %}
                        <span class="required">*</span>
                        {% endif %}
                    </label>
                    
                    {{ field }}
                    
                    <!-- Help text (aparece debajo del campo) -->
                    {% if field.help_text %}
                    <div class="help-text">{{ field.help_text }}</div>
                    {% endif %}
                    
                    <!-- Errores de validación HTML5 + Django -->
                    {% if field.errors %}
                    <div class="field-errors">
                        {% for error in field.errors %}
                        <span class="error-text">{{ error }}</span>
                        {% endfor %}
                    </div>
                    {% endif %}
                </div>
                {% endfor %}

                <div class="form-actions">
                    <button type="submit" class="btn btn-primary">
                        {% if form.instance.pk %}Actualizar{% else %}Crear{% endif %} Producto
                    </button>
                    <a href="{% url 'product_list' %}" class="btn btn-secondary">Cancelar</a>
                </div>
            </form>
        </div>
    </div>

    <!-- Mensaje de explicación para el usuario -->
    <div class="container">
        <div class="validation-info">
            <p> <strong>Validación automática:</strong> Este formulario valida automáticamente en tu navegador. 
            No se necesita JavaScript.</p>
        </div>
    </div>
</body>
</html>```

### `bookstore/products/templates/products/product_list.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bookstore - Productos</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="header">
        <div class="container">
            <h1>Nuestra Librería</h1>
        </div>
    </div>

    <div class="container">
        <!-- Botón para crear nuevo producto (como Rails) -->
        <div class="action-bar">
            <a href="{% url 'product_create' %}" class="btn btn-primary">
                Nuevo Producto
            </a>
        </div>

        {% if object_list %}
            <div class="products-grid">
                {% for product in object_list %}
                <div class="product-card">
                    {% if product.image %}
                    <img src="{{ product.image.url }}" alt="{{ product.title }}" class="product-image">
                    {% else %}
                    <div class="no-image">
                        <span> Sin imagen</span>
                    </div>
                    {% endif %}
                    
                    <h3 class="product-title">{{ product.title }}</h3>
                    <p class="product-description">{{ product.description }}</p>
                    <p class="product-price">${{ product.price }}</p>
                    
                    <!-- Acciones CRUD (como Rails Scaffold) -->
                    <div class="product-actions">
                        <a href="{% url 'product_detail' product.pk %}" class="btn btn-primary btn-sm">
                            Ver
                        </a>
                        <a href="{% url 'product_update' product.pk %}" class="btn btn-secondary btn-sm">
                            Editar
                        </a>
                        <a href="{% url 'product_delete' product.pk %}" class="btn btn-danger btn-sm">
                            Eliminar
                        </a>
                    </div>
                </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="no-products">
                <h2>No hay productos disponibles</h2>
                <p>¡Crea el primer producto!</p>
                <a href="{% url 'product_create' %}" class="btn btn-primary">Crear Producto</a>
            </div>
        {% endif %}
    </div>
</body>
</html>```

### `bookstore/static/css/style.css`
```css
/* static/css/style.css */
:root {
    --primary: #2563eb;
    --primary-dark: #1d4ed8;
    --text: #374151;
    --text-light: #6b7280;
    --background: #f9fafb;
    --white: #ffffff;
    --border: #e5e7eb;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', system-ui, sans-serif;
    line-height: 1.6;
    color: var(--text);
    background-color: var(--background);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.header {
    background: var(--white);
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    padding: 1rem 0;
    margin-bottom: 2rem;
}

.header h1 {
    color: var(--primary);
    font-size: 2rem;
    font-weight: 700;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.product-card {
    background: var(--white);
    border-radius: 0.5rem;
    padding: 1.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    transition: transform 0.2s, box-shadow 0.2s;
    border: 1px solid var(--border);
}

.product-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.product-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 0.375rem;
    margin-bottom: 1rem;
}

.product-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 0.5rem;
}

.product-description {
    color: var(--text-light);
    margin-bottom: 1rem;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.product-price {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 1rem;
}

.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border-radius: 0.375rem;
    text-decoration: none;
    font-weight: 600;
    text-align: center;
    transition: all 0.2s;
    border: none;
    cursor: pointer;
    font-size: 0.875rem;
}

.btn-primary {
    background-color: var(--primary);
    color: var(--white);
}

.btn-primary:hover {
    background-color: var(--primary-dark);
    transform: translateY(-1px);
}

.btn-secondary {
    background-color: var(--border);
    color: var(--text);
}

.btn-secondary:hover {
    background-color: #d1d5db;
}

.product-detail {
    background: var(--white);
    border-radius: 0.5rem;
    padding: 2rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    margin: 2rem 0;
}

.detail-image {
    max-width: 400px;
    width: 100%;
    border-radius: 0.5rem;
    margin-bottom: 1.5rem;
}

.no-products {
    text-align: center;
    padding: 3rem;
    color: var(--text-light);
}

/* Responsive */
@media (max-width: 768px) {
    .products-grid {
        grid-template-columns: 1fr;
    }
    
    .container {
        padding: 0 0.5rem;
    }
}

/* FORMULARIOS - Estilos como Rails */
.form-container {
    max-width: 600px;
    margin: 0 auto;
}

.product-form {
    background: var(--white);
    padding: 2rem;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--text);
}

.form-field {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid var(--border);
    border-radius: 0.375rem;
    font-size: 1rem;
    transition: all 0.2s;
}

.form-field:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-field.error {
    border-color: #dc2626;
    box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}

.field-errors {
    margin-top: 0.5rem;
}

.error-text {
    color: #dc2626;
    font-size: 0.875rem;
    display: block;
}

.form-actions {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
}

/* ACCIONES DE PRODUCTO */
.action-bar {
    margin-bottom: 2rem;
    padding: 1rem 0;
    border-bottom: 1px solid var(--border);
}

.product-actions {
    display: flex;
    gap: 0.5rem;
    margin-top: 1rem;
}

.btn-sm {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
}

.btn-danger {
    background-color: #dc2626;
    color: white;
}

.btn-danger:hover {
    background-color: #b91c1c;
}

/* ELIMINACIÓN */
.delete-confirmation {
    background: var(--white);
    padding: 2rem;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    text-align: center;
}

.product-preview {
    background: var(--background);
    padding: 1.5rem;
    border-radius: 0.375rem;
    margin: 1.5rem 0;
    border-left: 4px solid var(--primary);
}

.delete-form {
    margin-top: 2rem;
}

/* MEJORAS RESPONSIVE */
@media (max-width: 768px) {
    .product-actions {
        flex-direction: column;
    }
    
    .form-actions {
        flex-direction: column;
    }
    
    .btn-sm {
        text-align: center;
    }
}

/* ESTADOS DE VALIDACIÓN HTML5 */
.form-field:valid {
    border-color: #10b981;
    border-left: 4px solid #10b981;
}

.form-field:invalid:not(:focus):not(:placeholder-shown) {
    border-color: #dc2626;
    border-left: 4px solid #dc2626;
}

.form-field:focus:valid {
    border-color: #10b981;
    box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.form-field:focus:invalid {
    border-color: #dc2626;
    box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}

/* Indicador de campo requerido */
.required {
    color: #dc2626;
    font-weight: bold;
}

/* Texto de ayuda */
.help-text {
    font-size: 0.875rem;
    color: #6b7280;
    margin-top: 0.25rem;
    font-style: italic;
}

/* Mensajes de error mejorados */
.field-errors {
    margin-top: 0.5rem;
    padding: 0.5rem;
    background: #fef2f2;
    border: 1px solid #fecaca;
    border-radius: 0.375rem;
}

.error-text {
    color: #dc2626;
    font-size: 0.875rem;
    display: block;
}

/* Información de validación */
.validation-info {
    background: #eff6ff;
    border: 1px solid #dbeafe;
    border-radius: 0.5rem;
    padding: 1rem;
    margin-top: 2rem;
    text-align: center;
}

.validation-info p {
    margin: 0;
    color: #1e40af;
}

/* Estados de campos específicos */
input[type="number"]:out-of-range {
    border-color: #f59e0b;
    background: #fffbeb;
}

input:user-invalid {
    border-color: #dc2626;
}```

