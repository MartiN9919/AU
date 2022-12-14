# Generated by Django 4.1.2 on 2022-10-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItTechnicsType',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='Тип техники')),
            ],
            options={
                'verbose_name': 'Тип техники',
                'verbose_name_plural': 'Вид техники',
            },
        ),
        migrations.CreateModel(
            name='ModuleOrganization',
            fields=[
                ('parent_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=60, verbose_name='Наименование')),
                ('description', models.CharField(max_length=60, verbose_name='Описание')),
            ],
        ),
    ]
