# Generated by Django 3.2.9 on 2022-04-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]