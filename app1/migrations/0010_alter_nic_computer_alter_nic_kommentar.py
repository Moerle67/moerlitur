# Generated by Django 4.1.2 on 2022-11-03 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_nic_computer_alter_nic_kommentar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nic',
            name='computer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='app1.computer', verbose_name='Computer'),
        ),
        migrations.AlterField(
            model_name='nic',
            name='kommentar',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Kommentar'),
            preserve_default=False,
        ),
    ]