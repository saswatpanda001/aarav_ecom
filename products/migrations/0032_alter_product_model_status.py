# Generated by Django 3.2.4 on 2023-10-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_remove_featured_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_model',
            name='status',
            field=models.CharField(blank=True, choices=[('Sale', 'Sale'), ('New', 'New'), ('Out of Stock', 'Out of Stock'), ('Not Available', 'Not Available')], default='New', max_length=100, null=True),
        ),
    ]
