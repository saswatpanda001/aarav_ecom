# Generated by Django 3.2.4 on 2023-10-16 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_rename_balck_finding_product_model_back_finding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured',
            name='buyer',
        ),
    ]