# Generated by Django 4.1.2 on 2022-11-02 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_computer_hersteller'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbeitsspeicher',
            name='hersteller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='app1.hersteller', verbose_name='Hersteller'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='massenspeicher',
            name='hersteller',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.RESTRICT, to='app1.hersteller', verbose_name='Hersteller'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='massenspeicher',
            name='comment',
            field=models.CharField(blank=True, max_length=50, verbose_name='Kommentar'),
        ),
    ]
