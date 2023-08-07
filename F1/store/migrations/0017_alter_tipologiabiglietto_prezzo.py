# Generated by Django 4.2.2 on 2023-08-07 14:57

import F1.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_tipologiabiglietto_prezzo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipologiabiglietto',
            name='prezzo',
            field=models.FloatField(default=0.0, validators=[F1.validators.valida_non_negativi]),
        ),
    ]