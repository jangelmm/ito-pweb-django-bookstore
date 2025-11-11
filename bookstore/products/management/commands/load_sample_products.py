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
                )