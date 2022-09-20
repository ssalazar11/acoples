# Generated by Django 4.1.1 on 2022-09-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
                ('unidad', models.CharField(max_length=20)),
                ('valorUnidad', models.IntegerField()),
            ],
        ),
    ]