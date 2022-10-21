from tabnanny import verbose
from django.contrib import admin
from .models import ItTechnicsModels
from django.utils.safestring import mark_safe

@admin.register(ItTechnicsModels)
class ItTechnicsModels(admin.ModelAdmin):

    list_display = (
        'id',
        'type',
        'id_name',
        'date_start',
        'date_end',
        'date_max',
        # 'decommissioning_date',
        'organization',
        'get_image',
          
    )


    list_filter = ('type','organization',)
    list_editable = ()
    list_per_page = 20
    search_fields = (
    )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}">')
    get_image.short_description = "Изображение"
