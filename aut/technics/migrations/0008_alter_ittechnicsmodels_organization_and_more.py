# Generated by Django 4.1.2 on 2022-10-28 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_tech', '0003_alter_moduleorganization_options'),
        ('technics', '0007_alter_ittechnicsmodels_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ittechnicsmodels',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='list_tech.moduleorganization', verbose_name='В/Ч'),
        ),
        migrations.AlterField(
            model_name='ittechnicsmodels',
            name='type',
            field=models.ForeignKey(db_column='name', on_delete=django.db.models.deletion.CASCADE, related_name='type', to='list_tech.ittechnicstype', verbose_name='Тип'),
        ),
    ]
