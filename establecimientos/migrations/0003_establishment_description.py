# Generated by Django 3.0.6 on 2020-07-22 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimientos', '0002_auto_20200720_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='description',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
    ]
