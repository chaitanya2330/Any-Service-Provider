# Generated by Django 2.0.6 on 2019-03-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prize',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
