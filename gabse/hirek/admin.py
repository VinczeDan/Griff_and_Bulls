# hirek/admin.py
from django.contrib import admin
from .models import Hir
from .models import Meccs
from .models import PDFDocument

@admin.register(Hir)
class HirAdmin(admin.ModelAdmin):
    list_display = ('cim', 'letrehozva', 'publikalt')
    prepopulated_fields = {'slug': ('cim',)}
    list_filter = ('publikalt', 'letrehozva')
    search_fields = ('cim', 'tartalom')

@admin.register(Meccs)
class MeccsAdmin(admin.ModelAdmin):
    list_display = ('korosztaly', 'hazai_csapat', 'vendeg_csapat', 'eredmeny', 'datum', 'tipus')
    list_filter = ('tipus', 'korosztaly')
    search_fields = ('hazai_csapat', 'vendeg_csapat')
    fieldsets = (
        (None, {
            'fields': ('tipus', 'korosztaly', 'datum')
        }),
        ('Meccs adatai', {
            'fields': ('hazai_csapat', 'vendeg_csapat', 'eredmeny', 'helyszin', 'idopont')
        }),
    )


@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)
    list_filter = ('uploaded_at',)