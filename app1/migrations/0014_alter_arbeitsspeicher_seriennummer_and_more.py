# Generated by Django 4.1.2 on 2022-11-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_arbeitsspeicher_computer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbeitsspeicher',
            name='seriennummer',
            field=models.CharField(max_length=50, null=True, verbose_name='SN'),
        ),
        migrations.AlterField(
            model_name='nic',
            name='kommentar',
            field=models.CharField(max_length=50, null=True, verbose_name='Kommentar'),
        ),
    ]
