# Generated by Django 3.2.9 on 2022-05-26 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220525_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='rg',
            field=models.CharField(max_length=13),
        ),
    ]
