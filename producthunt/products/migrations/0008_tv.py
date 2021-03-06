# Generated by Django 2.0.6 on 2019-03-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_mobile_votes_total1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=255)),
                ('image2', models.ImageField(upload_to='images/')),
                ('icon2', models.ImageField(upload_to='images/')),
                ('body2', models.TextField()),
                ('prize2', models.CharField(max_length=255, null=True)),
                ('votes_total2', models.IntegerField(default=1)),
            ],
        ),
    ]
