# Generated by Django 2.0.2 on 2020-07-27 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establecimientos', '0004_establishment_id_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Nombre')),
                ('content', models.TextField(verbose_name='Opinión')),
                ('score', models.PositiveIntegerField(verbose_name='Estrellas')),
                ('id_establecimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='establecimientos.Establishment')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]
