# Generated by Django 4.1.2 on 2022-11-07 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_nic_computer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massenspeicher',
            name='computer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='app1.computer', verbose_name='Computer'),
        ),
    ]
