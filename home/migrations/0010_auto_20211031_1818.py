# Generated by Django 3.2.8 on 2021-10-31 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_products_product_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Offers',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
