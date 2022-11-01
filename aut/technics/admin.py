from email.headerregistry import Group
from tabnanny import verbose
from django.contrib import admin
from .models import ItTechnicsModels
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group
from docx import Document
from django.contrib import messages
from django.utils.translation import ngettext


@admin.action(description="Выгрузка отчета в Word")
def get_report(modeladmin,request, queryset):
    qs = queryset.values('id', 'type__name', 'id_name', 'organization__name')
    doc = Document()
    table = doc.add_table(rows=1, cols=len(qs[0]))
    row = table.rows[0]
    row.cells[0].text = 'ID'
    row.cells[1].text = 'Наименование техники'
    row.cells[2].text = 'Инвентарный номер'
    row.cells[3].text = 'Подразделение'
    for query in qs:
        row_cells = table.add_row().cells
        for i, value in enumerate(query.values()):
            row_cells[i].text = str(value)

    doc.save("test2.docx")
    messages.add_message(request, messages.INFO, "Отчет сформирован")


@admin.register(ItTechnicsModels)
class ItTechnicsModelsAdmin(admin.ModelAdmin):
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
        group = str(request.user.groups.get())
        if group == 'ГПК':
            return super().get_queryset(request)
        else:
            return super().get_queryset(request).filter(organization__name='в/ч' + ' ' + group)

        



    list_filter = ('type','organization',)
    list_editable = ()
    list_per_page = 20
    search_fields = (  )
    actions = [get_report]
    

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.img.url}">')
    get_image.short_description = "Изображение"

