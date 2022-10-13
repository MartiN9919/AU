from django.contrib import admin
from .models import ItTechnicsModels,ModuleOrganization



@admin.register(ItTechnicsModels)
class ItTechnicsModels(admin.ModelAdmin):
    list_display = (
        'name',
        'add_date',
        'categorian',
        'organization',
    )

    list_filter = ('name', 'categorian', 'add_date',)
    list_editable = ('categorian', 'add_date','organization',)
    list_per_page = 20

@admin.register(ModuleOrganization)
class ModuleOrganization(admin.ModelAdmin):
    list_display = (
        'parent_id',
        'name',
        'description',
    )

    list_filter = ('name', 'description',)
    list_per_page = 30