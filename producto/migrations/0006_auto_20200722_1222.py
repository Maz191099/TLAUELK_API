# Generated by Django 3.0.6 on 2020-07-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_auto_20200722_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='Imagen'),
        ),
    ]
