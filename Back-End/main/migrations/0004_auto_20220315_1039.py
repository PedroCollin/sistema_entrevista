# Generated by Django 3.2.9 on 2022-03-15 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220315_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='dataFechamento',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 10, 39, 7, 981513), null=True),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='dataInicio',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 10, 39, 7, 981513)),
        ),
    ]