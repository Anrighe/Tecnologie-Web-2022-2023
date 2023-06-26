# Generated by Django 4.2.1 on 2023-06-23 17:27

import F1.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_utente_carta_credito_alter_utente_cvv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utente',
            name='carta_credito',
            field=models.CharField(blank=True, default=None, max_length=19, null=True, validators=[F1.validators.valida_carta_credito]),
        ),
        migrations.AlterField(
            model_name='utente',
            name='cvv',
            field=models.CharField(blank=True, default=None, max_length=3, null=True, validators=[F1.validators.valida_cvv]),
        ),
        migrations.AlterField(
            model_name='utente',
            name='immagine_profilo',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='utente',
            name='indirizzo',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='utente',
            name='paese',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='utente',
            name='scadenza_carta',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='utente',
            name='telefono',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
    ]