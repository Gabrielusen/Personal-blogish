# Generated by Django 2.2.2 on 2020-02-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
