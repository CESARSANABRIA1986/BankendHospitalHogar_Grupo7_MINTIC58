# Generated by Django 4.1.1 on 2022-09-27 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0008_account_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='descripcion',
            field=models.CharField(max_length=250, verbose_name='Descripcion'),
        ),
    ]