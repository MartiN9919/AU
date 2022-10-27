from django.db import models
from django.contrib import admin

# Create your models here.


class ItTechnicsType(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='id',
        db_column = 'id',

    )
    name= models.CharField(
        max_length=60,
        verbose_name='Тип техники',
        blank=True
    )

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Тип техники"
        verbose_name_plural = "Тип техники"


class ModuleOrganization(models.Model):
    """
    Класс для описания модели по направлению деятельности
    """
    parent_id = models.AutoField(
        primary_key=True,
        verbose_name='id',
        unique=True,

    )
    name = models.CharField(
        max_length=60,
        verbose_name='Наименование',
    )

    description = models.CharField(
        max_length=60,
        verbose_name='Описание',
    )

    class Meta:
        verbose_name = "Наименование организации"
        verbose_name_plural = "Наименование организации"

    def __str__(self):
        return self.name