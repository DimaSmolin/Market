# Generated by Django 5.0.1 on 2024-02-08 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0026_alter_store_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')),
                ('alt', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Галлерея',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]