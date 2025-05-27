# hirek/admin.py
from django.contrib import admin
from .models import Hir
from .models import Meccs
from .models import PDFDocument
from .models import Jatekos, Edzo, Korosztaly





@admin.register(Edzo)
class EdzoAdmin(admin.ModelAdmin):
    list_display = ('nev', 'pozicio', 'tipus')
    list_filter = ('tipus', 'korosztalyok')
    filter_horizontal = ('korosztalyok',)
    search_fields = ('nev', 'pozicio')


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



class JatekosInline(admin.TabularInline):
    model = Jatekos
    extra = 1


@admin.register(Korosztaly)
class KorosztalyAdmin(admin.ModelAdmin):
    list_display = ('nev',   'sorrend')
    prepopulated_fields = {'slug': ('nev',)}
    inlines = [JatekosInline]
    
    def vezeto_edzo(self, obj):
        edzo = obj.vezeto_edzo()
        return edzo.nev if edzo else "-"
    vezeto_edzo.short_description = 'Vezető edző'
    
    def asszisztens_edzo(self, obj):
        asszisztens = obj.asszisztens_edzo()
        return asszisztens.nev if asszisztens else "-"
    asszisztens_edzo.short_description = 'Asszisztens edző'

@admin.register(Jatekos)
class JatekosAdmin(admin.ModelAdmin):
    list_display = ('nev', 'korosztaly', 'get_poszt_display', 'mezszam')
    list_filter = ('korosztaly', 'poszt')
    search_fields = ('nev',)