# Generated by Django 3.2.8 on 2021-10-21 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_products_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offers',
            old_name='main_Seller',
            new_name='main_seller',
        ),
    ]
