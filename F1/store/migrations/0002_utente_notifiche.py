# Generated by Django 4.2.1 on 2023-05-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utente',
            name='notifiche',
            field=models.BooleanField(default=False),
        ),
    ]
