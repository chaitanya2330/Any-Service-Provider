# Generated by Django 2.0.6 on 2019-03-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
    ]
