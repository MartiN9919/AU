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


class ItTechnicsType(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='id',
        unique=True,
    )
    name= models.CharField(
        max_length=60,
        verbose_name='Тип техники',
    )

    description= models.CharField(
        max_length=60,
        verbose_name='Дополнительное описание',
        blank=True

    )

    def __str__(self):
        return self.name

class ItTechnicsModels(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='№',

    )
    type = models.ForeignKey(
        ItTechnicsType,
        on_delete=models.CASCADE,
        db_column='name',
        verbose_name='Наименование Техники',
    )
    id_name = models.CharField(
        max_length=60,
        verbose_name='Инвентарный номер',
    )
    date_start =models.DateField(
        verbose_name='Дата ввода в эксплуатацию',
        null=True,
    )
    date_end = models.DateField(
        verbose_name='Дата окончания',
        null=True,
    )
    date_max = models.DurationField(
        verbose_name='MAX Период эксплуатации',
        null=True,
    )
    decommissioning_date = models.DateField(
        verbose_name='Дата вывода из эксплуатации',
        null=True,
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
    SIZES = (
                ('Отсутствует', 'Отсутствует'),
                ('Изъято', 'Изъято'),
                ('В наличии/не изымалось', 'В наличии/не изымалось'),
            )
    wifi_availability = models.CharField(
        max_length= 100,
        choices=SIZES,
    )

    date_shutdown = models.DateField(
        verbose_name='Дата Изъятия модуля БПД',
        null=True,
    )

    serial_numbers_device = models.CharField(
        max_length=60,
        verbose_name=' Серийный номер модуля',
    )

    img = models.ImageField(
        null=True,
        upload_to='products_images',
        verbose_name='Изображение',
        blank=True,
     )
    number_information = models.CharField(
        max_length= 7,
        verbose_name='Номер СВТ',
    )

    date_start_Kanoe = models.DateField(
        verbose_name='Дата установки ПО КАНОЭ',
        null=True,
    )
    date_end_Kanoe = models.DateField(
        verbose_name='Дата окончания ПО КАНОЭ',
        null=True,
    )
