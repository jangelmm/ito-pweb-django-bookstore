from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'price']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Título del producto'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-field',
                'rows': 4,
                'placeholder': 'Descripción del producto'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-field',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-field'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar clases CSS dinámicas basadas en validación (como Rails)
        for field_name, field in self.fields.items():
            if self.instance.pk and field_name in self.errors:
                field.widget.attrs['class'] = 'form-field error'