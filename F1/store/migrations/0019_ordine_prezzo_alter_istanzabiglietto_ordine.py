# Generated by Django 4.2.2 on 2023-08-08 14:27

import F1.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_ordine_gestore_circuito'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordine',
            name='prezzo',
            field=models.FloatField(default=0.0, validators=[F1.validators.valida_non_negativi]),
        ),
        migrations.AlterField(
            model_name='istanzabiglietto',
            name='ordine',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.ordine'),
        ),
    ]
