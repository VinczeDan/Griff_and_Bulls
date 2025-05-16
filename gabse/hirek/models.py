# hirek/models.py
from django.db import models
from django.utils import timezone, text

class Hir(models.Model):
    cim = models.CharField(max_length=200, unique=True)  # Egyedi címek
    slug = models.SlugField(max_length=200, unique=True)
    tartalom = models.TextField()
    kiemelt_kep = models.ImageField(
        upload_to='media/hirek_kepek',  # A media/ mappán belüli útvonal
        blank=True,  # Nem kötelező
        null=True    # Lehet üres az adatbázisban
    )
    letrehozva = models.DateTimeField(default=timezone.now)
    publikalt = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.cim)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.cim

    class Meta:
        ordering = ['-letrehozva']
        verbose_name_plural = 'Hírek'

class Meccs(models.Model):
    TIPUS_CHOICES = [
        ('EREDMENY', 'Eredmény'),
        ('KOVETKEZO', 'Következő meccs'),
    ]
    
    tipus = models.CharField(max_length=10, choices=TIPUS_CHOICES)
    korosztaly = models.CharField(max_length=50)
    hazai_csapat = models.CharField(max_length=100)
    vendeg_csapat = models.CharField(max_length=100)
    eredmeny = models.CharField(max_length=20, blank=True)
    datum = models.DateField()
    helyszin = models.CharField(max_length=100, blank=True)
    idopont = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Meccsek"
        ordering = ['-datum']

    def __str__(self):
        if self.tipus == 'EREDMENY':
            return f"{self.hazai_csapat} {self.eredmeny} {self.vendeg_csapat}"
        return f"{self.hazai_csapat} vs {self.vendeg_csapat}"

class PDFDocument(models.Model):
    title = models.CharField(max_length=200, verbose_name="Dokumentum neve")
    file = models.FileField(upload_to='pdfs/', verbose_name="PDF fájl")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Feltöltve")

    class Meta:
        verbose_name = "PDF dokumentum"
        verbose_name_plural = "PDF dokumentumok"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title