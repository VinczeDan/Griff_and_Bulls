# hirek/views.py
from django.shortcuts import render, get_object_or_404
from .models import Hir
from .models import Hir, Meccs
from .models import PDFDocument

# hirek/views.py

def fooldal(request):
    # Hírek lekérése (a meglévő logika marad)
    legfrissebb_hirek = Hir.objects.filter(publikalt=True).order_by('-letrehozva').distinct()[:3]
    
    # Új adatok: eredmények és következő meccsek
    eredmenyek = Meccs.objects.filter(tipus='EREDMENY').order_by('-datum')[:5]
    kovetkezo_meccsek = Meccs.objects.filter(tipus='KOVETKEZO').order_by('datum')[:5]
    
    # Összes adat átadása a template-nek
    return render(request, "hirek/index.html", {
        'hirek': legfrissebb_hirek,
        'eredmenyek': eredmenyek,
        'kovetkezo_meccsek': kovetkezo_meccsek
    })

def hirek_oldal(request):
    osszes_hir = Hir.objects.filter(publikalt=True).order_by('-letrehozva')
    return render(request, "hirek/hirek.html", {'hirek': osszes_hir})

def hir_reszletek(request, slug):
    hir = get_object_or_404(Hir, slug=slug, publikalt=True)
    legfrissebb_hirek = Hir.objects.filter(publikalt=True).exclude(id=hir.id).order_by('-letrehozva')[:3]
    return render(request, "hirek/hir.html", {
        'hir': hir,
        'legfrissebb_hirek': legfrissebb_hirek
    })

# Meglévő view-k megtartása
def edzok(request):
    return render(request, "hirek/edzok.html")

def csapataink(request):
    return render(request, "hirek/csapatok.html")

def u19(request):
    return render(request, "hirek/u19.html")

def u17(request):
    return render(request, "hirek/u17.html")

def u16(request):
    return render(request, "hirek/u16.html")

def u15(request):
    return render(request, "hirek/u15.html")

def u11(request):
    return render(request, "hirek/u11.html")

def felnott(request):
    return render(request, "hirek/felnott.html")

def oldboys(request):
    return render(request, "hirek/oldboys.html")

def oregfiuk(request):
    return render(request, "hirek/oregfiuk.html")

def aktualis(request):
    osszes_hir = Hir.objects.filter(publikalt=True).order_by('-letrehozva')
    return render(request, "hirek/aktualis.html", {'hirek': osszes_hir})



def palyazat(request):
    pdfs = PDFDocument.objects.all().order_by('-uploaded_at')  # Összes PDF dátum szerint rendezve
    return render(request, 'hirek/palyazat.html', {'pdfs': pdfs})