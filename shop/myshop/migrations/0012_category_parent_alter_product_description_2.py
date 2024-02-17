# Generated by Django 4.2.6 on 2023-12-17 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0011_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='myshop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_2',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
