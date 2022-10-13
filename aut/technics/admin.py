from django.contrib import admin
from .models import ItTechnicsModels, ModuleOrganization



@admin.register(ItTechnicsModels)
class ItTechnicsModels(admin.ModelAdmin):
    list_display = (
        'name',
        'name1',
        'add_date',
        'categorian',
        'organization',
        'img'
    )

    list_filter = ('name','name1', 'categorian', 'add_date','organization',)
    list_editable = ('categorian', 'add_date','organization','name1',)
    list_per_page = 20
    search_fields = (
       'add_date',
    )



@admin.register(ModuleOrganization)
class ModuleOrganization(admin.ModelAdmin):
    list_display = (
        'parent_id',
        'name',
        'description',
    )

    list_filter = ('name', 'description',)
    list_per_page = 30