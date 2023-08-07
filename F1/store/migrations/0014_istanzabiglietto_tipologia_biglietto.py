# Generated by Django 4.1.7 on 2023-08-05 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_tipologiabiglietto_istanza_biglietto'),
    ]

    operations = [
        migrations.AddField(
            model_name='istanzabiglietto',
            name='tipologia_biglietto',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.tipologiabiglietto'),
        ),
    ]