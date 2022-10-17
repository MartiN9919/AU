from django.contrib import admin
from .models import ItTechnicsModels, ModuleOrganization, ItTechnicsType


@admin.register(ItTechnicsType)
class ItTechnicsType(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
    )

    list_filter = ('name', 'description',)
    list_per_page = 30
@admin.register(ItTechnicsModels)
class ItTechnicsModels(admin.ModelAdmin):

    list_display = (
        'id',
        'type',
        'id_name',
        'date_start',
        'date_end',
        'date_max',
        'decommissioning_date',
        'categorian',
        'organization',
        'img',
        'wifi_availability',
        'date_shutdown',
        'serial_numbers_device',
        'number_information',
        'date_start_Kanoe',
        'date_end_Kanoe',
    )

    list_select_related = True

    list_filter = ('type','categorian',)
    list_editable = ()
    list_per_page = 20
    search_fields = (
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

