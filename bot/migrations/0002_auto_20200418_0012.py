# Generated by Django 3.0.5 on 2020-04-18 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.IntegerField(unique=True, verbose_name='ID Telegram'),
        ),
    ]
