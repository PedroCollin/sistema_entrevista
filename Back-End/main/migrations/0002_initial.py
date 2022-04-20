# Generated by Django 3.2.9 on 2022-04-19 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='respostadinamica',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='respostadinamica',
            name='vagaDinamica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vagadinamica'),
        ),
        migrations.AddField(
            model_name='entrevista',
            name='candidato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.candidato'),
        ),
        migrations.AddField(
            model_name='entrevista',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.statusentrevista'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cidade'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='vaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vaga'),
        ),
        migrations.AddField(
            model_name='avaliacaodinamica',
            name='dinamica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dinamica'),
        ),
        migrations.AddField(
            model_name='aprovacaodinamica',
            name='candidato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.candidato'),
        ),
        migrations.AddField(
            model_name='aprovacaodinamica',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]