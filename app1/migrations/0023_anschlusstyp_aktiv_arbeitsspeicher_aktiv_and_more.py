# Generated by Django 4.1.2 on 2022-11-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_tool_bezeichnung_alter_tool_zusatzinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='anschlusstyp',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='arbeitsspeicher',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='arbeitsspeichertyp',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='einsatzgebiet',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='einsatzmoeglichkeit',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hersteller',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='massenspeicher',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='massenspeichertyp',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='nic',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='nictyp',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ort',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='prozessor',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='raum',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sorte',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='speicherart',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='standort',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tooltyp',
            name='aktiv',
            field=models.BooleanField(default=True),
        ),
    ]
