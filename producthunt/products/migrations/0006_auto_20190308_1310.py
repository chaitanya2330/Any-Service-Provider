# Generated by Django 2.0.6 on 2019-03-08 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='title1',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='hunter1',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='pub_date1',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='url1',
        ),
        migrations.RemoveField(
            model_name='mobile',
            name='video1',
        ),
    ]
