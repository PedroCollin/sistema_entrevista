# Generated by Django 3.2.9 on 2022-03-15 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220315_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='dataFechamento',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 11, 7, 11, 776496), null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 11, 7, 11, 776496)),
        ),
    ]