# Generated by Django 2.0.5 on 2018-05-30 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ensino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='A etapa do ensino na educação em que a série está inserida, ex: Ensino Médio, Fundamental, EJA', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Organizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da série, ex: Jardim 1', max_length=100)),
                ('ensino', models.ForeignKey(help_text='A etapa do ensino em que a série está inserida', on_delete=django.db.models.deletion.CASCADE, to='core.Ensino')),
            ],
        ),
        migrations.AddField(
            model_name='instituicao',
            name='organizacao',
            field=models.ForeignKey(help_text='A organização que essa instituição de ensino faz parte, ex: Prefeitura de São Judas', on_delete=django.db.models.deletion.CASCADE, to='core.Organizacao'),
        ),
        migrations.AddField(
            model_name='componente',
            name='ensino',
            field=models.ForeignKey(help_text='A etapa do ensino em que este componente está inserido', on_delete=django.db.models.deletion.CASCADE, to='core.Ensino'),
        ),
        migrations.AddField(
            model_name='componente',
            name='organizacao',
            field=models.ForeignKey(help_text='A organização que a escola faz parte, ex: Prefeitura de São Judas', on_delete=django.db.models.deletion.CASCADE, to='core.Organizacao'),
        ),
    ]
