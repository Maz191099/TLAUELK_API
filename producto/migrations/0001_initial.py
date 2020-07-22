# Generated by Django 2.1 on 2020-07-22 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='imageprod', verbose_name='Imagen')),
                ('description', models.TextField()),
            ],
        ),
    ]