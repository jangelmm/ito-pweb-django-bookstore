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
        return price