from django.db import models


# Create your models here.

class ModuleOrganization(models.Model):
    """
    Класс для описания модели линии доступа по направлению деятельности
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

    def __str__(self):
        return self.name




class ItTechnicsModels(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Наименование Техники',
    )
    add_date = models.DateField(
        verbose_name='Дата постановки на учёт',
    )

    categorian = models.BooleanField(
        verbose_name='Категорированная',
    )
    organization= models.ForeignKey(
        ModuleOrganization,
        verbose_name='Организация',
        on_delete=models.CASCADE,
        null=True,

    )

    name1 = models.CharField(
        max_length=60,
        verbose_name='Наименование Техники',
    )
    img = models.ImageField(
        upload_to='products_images',
        verbose_name='Изображение'


     )
