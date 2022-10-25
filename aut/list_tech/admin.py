from tabnanny import verbose
from django.contrib import admin
from .models import ModuleOrganization, ItTechnicsType
# Register your models here.

@admin.register(ModuleOrganization)
class ModuleOrganization(admin.ModelAdmin):
    list_display = (
      
        'parent_id',
        'name',
    )
    list_filter = ('name',)
    list_per_page = 30


    class Meta:
        verbose_name_plural = 'Организации'
        verbose_name = 'Организации'
    
  

@admin.register(ItTechnicsType)
class ItTechnicsType(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    
    )

    list_filter = ('name',)
    list_per_page = 30
# Register your models here.
    class Meta:
        verbose_name_plural = 'Виды компьютерной техники'
        verbose_name = 'Виды Компьютерной техники'
 