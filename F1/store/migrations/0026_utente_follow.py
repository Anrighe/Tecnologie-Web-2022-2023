# Generated by Django 4.2.4 on 2023-08-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_circuito_data_evento'),
        ('store', '0025_ordine_biglietto_digitale'),
    ]

    operations = [
        migrations.AddField(
            model_name='utente',
            name='follow',
            field=models.ManyToManyField(blank=True, default=None, to='info.scuderia'),
        ),
    ]
