# hirek/models.py
from django.db import models
from django.utils import timezone, text

class Hir(models.Model):
    cim = models.CharField(max_length=200, unique=True)  
    slug = models.SlugField(max_length=200, unique=True)
    tartalom = models.TextField()
    kiemelt_kep = models.ImageField(
        upload_to='media/hirek_kepek',  
        blank=True,  
        null=True    
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
    

class Korosztaly(models.Model):
    nev = models.CharField("Korosztály neve", max_length=100)
    slug = models.SlugField(unique=True)
    sorrend = models.PositiveIntegerField("Sorrend", default=0)

    class Meta:
        verbose_name = "Korosztály"
        verbose_name_plural = "Korosztályok"
        ordering = ['sorrend']

    def __str__(self):
        return self.nev


class Edzo(models.Model):
    TIPUS_CHOICES = [
        ('edzo', 'Edző'),
        ('szakmai', 'Szakmai Stáb'),
    ]
    
    nev = models.CharField("Név", max_length=250)
    pozicio = models.CharField("Pozíció", max_length=250)
    tipus = models.CharField("Típus", max_length=10, choices=TIPUS_CHOICES)
    korosztalyok = models.ManyToManyField(Korosztaly, blank=True, verbose_name="Vezetett korosztályok")

    class Meta:
        verbose_name = "Edző/Szakmai tag"
        verbose_name_plural = "Edzők/Szakmai stáb"

    def __str__(self):
        return self.nev



class Jatekos(models.Model):
    POSZT_CHOICES = [
        ('K', 'Kapus'),
        ('V', 'Védő'),
        ('KP', 'Középpályás'),
        ('T', 'Támadó'),
    ]
    
    nev = models.CharField(max_length=250)
    korosztaly = models.ForeignKey(Korosztaly, on_delete=models.CASCADE, related_name='jatekosok')
    poszt = models.CharField(max_length=2, choices=POSZT_CHOICES)
    mezszam = models.PositiveSmallIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Jatekos"
        verbose_name_plural = "Jatekosok"

    def __str__(self):
        return f"{self.nev} ({self.get_poszt_display()})"