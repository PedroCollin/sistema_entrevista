# Generated by Django 3.2.9 on 2022-05-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_curso_imgcurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='foto',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='imgCurso',
            field=models.TextField(default='None'),
        ),
    ]