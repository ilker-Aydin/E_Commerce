# Generated by Django 5.1 on 2024-08-30 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoEcommerce', '0012_remove_product_image_product_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
    ]
