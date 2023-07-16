# Generated by Django 4.2.2 on 2023-07-10 10:35

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_scuderia_campionati_vinti_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pilota',
            name='eta',
        ),
        migrations.RemoveField(
            model_name='pilota',
            name='foto',
        ),
        migrations.AddField(
            model_name='pilota',
            name='biografia',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='pilota',
            name='campionati_vinti',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pilota',
            name='foto_casco',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pilota',
            name='foto_pilota',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pilota',
            name='immagine1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pilota',
            name='immagine2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='pilota',
            name='numero_gare',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pilota',
            name='paese',
            field=django_countries.fields.CountryField(blank=True, default=None, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='pilota',
            name='podi',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scuderia',
            name='descrizione',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='scuderia',
            name='immagine1',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='scuderia',
            name='immagine2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
