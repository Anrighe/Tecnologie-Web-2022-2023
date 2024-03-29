# Generated by Django 4.2.1 on 2023-06-26 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_utente_immagine_profilo'),
    ]

    operations = [
        migrations.AddField(
            model_name='utente',
            name='data_nascita',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='biglietto',
            name='data_evento',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='notifica',
            name='data',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ordine',
            name='data',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='utente',
            name='premium',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='utente',
            name='scadenza_carta',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
