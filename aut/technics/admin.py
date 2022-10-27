from email.headerregistry import Group
from tabnanny import verbose
from django.contrib import admin
from .models import ItTechnicsModels
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group
@admin.register(ItTechnicsModels)
class ItTechnicsModels(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'id_name',
        'date_start',
        'date_end',
        'date_max',
        'organization',
        'get_image',

    )

    def get_queryset(self, request):
        if request.user.groups.filter(name='2044').exists():
            return super().get_queryset(request).filter(organization=2)
        else:
            return super().get_queryset(request)

          


    list_filter = ('type','organization',)
    list_editable = ()
    list_per_page = 20
    search_fields = (  )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}">')
    get_image.short_description = "Изображение"
    