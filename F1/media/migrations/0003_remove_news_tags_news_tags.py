# Generated by Django 4.2.4 on 2023-08-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_circuito_data_evento'),
        ('media', '0002_remove_news_autore_remove_news_contenuto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='tags',
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='info.scuderia'),
        ),
    ]
