# Generated by Django 4.1.2 on 2022-11-07 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_alter_tool_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.RESTRICT, to='app1.tooltyp', verbose_name='Typ'),
            preserve_default=False,
        ),
    ]