# Generated by Django 4.1.2 on 2022-10-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technics', '0004_alter_ittechnicsmodels_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ittechnicsmodels',
            name='id_name',
            field=models.CharField(max_length=60, null=True, verbose_name='Инвентарный №_ИТ'),
        ),
    ]
