# Generated by Django 4.2.1 on 2023-05-13 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=254)),
                ('image', models.ImageField(upload_to='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Insident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(choices=[('IN', 'Incident'), ('RQ', 'Request')], max_length=2)),
                ('level', models.CharField(choices=[('Low', 'Bajo'), ('Mid', 'Medio'), ('Hi', 'Alta'), ('VHi', 'Critico')], max_length=3)),
                ('url', models.URLField()),
                ('project', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('cel_phone', models.CharField(max_length=12)),
            ],
        ),
    ]