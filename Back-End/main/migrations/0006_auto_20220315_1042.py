# Generated by Django 3.2.9 on 2022-03-15 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220315_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='dataFechamento',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 10, 42, 36, 258885), null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 10, 42, 36, 258885)),
        ),
    ]
