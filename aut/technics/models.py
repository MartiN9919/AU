from django.db import models
from docx import Document
from list_tech.models import ModuleOrganization, ItTechnicsType


class ItTechnicsModels(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='№',
        
    )
    type = models.ForeignKey(
        ItTechnicsType,
        on_delete=models.CASCADE,
        db_column='name',
        verbose_name='Тип',
        related_name='type'
    
    )
    id_name = models.CharField(
        max_length=60,
        verbose_name='Инвентарный №_ИТ',
        null=True,
    )
    date_start =models.DateField(
        verbose_name='Ввод в эксплуатацию',
        null=True,
    )
    date_end = models.DateField(
        verbose_name='Вывод из эксплуатации',
        null=True,
    )
    date_max = models.DurationField(
        verbose_name='MAX Период эксплуатации',
        null=True,
    )
    # decommissioning_date = models.DateField(
    #     verbose_name='Дата вывода из эксплуатации',
    #     null=True,
    # )

    organization= models.ForeignKey(
        ModuleOrganization,
        verbose_name='В/Ч',
        on_delete=models.CASCADE,
        null=True,
        related_name='organization'    
    )
    SIZES = (
                ('Отсутствует', 'Отсутствует'),
                ('Изъято', 'Изъято'),
                ('В наличии/не изымалось', 'В наличии/не изымалось'),
            )
    wifi_availability = models.CharField(
        verbose_name="Wifi",
        max_length= 100,
        choices=SIZES,  
        null=True,
    )

    date_shutdown = models.DateField(
        verbose_name='Изъятие WIFI',
        null=True,
    )


    img = models.ImageField(
        null=True,
        upload_to='products_images',
        verbose_name='Файл',
        blank=True,
     )
    number_information = models.CharField(
        max_length= 7,
        verbose_name='Номер СВТ',
        null = True,)

    date_start_Kanoe = models.DateField(
        verbose_name='Установка ПО КАНОЭ',
        null=True,
    )
    date_end_Kanoe = models.DateField(
        verbose_name='Окончание ПО КАНОЭ',
        null=True,
    )

 
    class Meta:
        verbose_name = "Технику"
        verbose_name_plural = "Техника"


