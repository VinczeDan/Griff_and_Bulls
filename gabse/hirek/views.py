
# hirek/views.py
from django.shortcuts import render, get_object_or_404
from .models import Hir
from .models import Hir, Meccs
from .models import PDFDocument 
from .models import Korosztaly
from .models import Edzo

# hirek/views.py

def fooldal(request):
    # Hírek lekérése (a meglévő logika marad)
    legfrissebb_hirek = Hir.objects.filter(publikalt=True).order_by('-letrehozva').distinct()[:3]
    
    # Új adatok: eredmények és következő meccsek
    eredmenyek = Meccs.objects.filter(tipus='EREDMENY').order_by('-datum')[:5]
    kovetkezo_meccsek = Meccs.objects.filter(tipus='KOVETKEZO').order_by('datum')[:5]
    korosztalyok = Korosztaly.objects.all()

    # Összes adat átadása a template-nek
    return render(request, "hirek/index.html", {
        'hirek': legfrissebb_hirek,
        'eredmenyek': eredmenyek,
        'kovetkezo_meccsek': kovetkezo_meccsek,
        'korosztalyok': korosztalyok,
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


def edzok(request):
    return render(request, "hirek/edzok.html")

def csapataink(request):
    return render(request, "hirek/csapatok.html")

def korosztaly(request, korosztaly_slug: str):
    korosztaly = get_object_or_404(Korosztaly, slug=korosztaly_slug)
    
    jatekosok = korosztaly.jatekosok.all()
    posztok = {
        'Kapusok': jatekosok.filter(poszt='K'),
        'Védők': jatekosok.filter(poszt='V'),
        'Középpályások': jatekosok.filter(poszt='KP'),
        'Támadók': jatekosok.filter(poszt='T'),
    }
    
    context = {
        'korosztaly': korosztaly,
        'posztok': posztok,
    }
    return render(request, "hirek/korosztaly.html", context)

def aktualis(request):
    osszes_hir = Hir.objects.filter(publikalt=True).order_by('-letrehozva')
    return render(request, "hirek/aktualis.html", {'hirek': osszes_hir})



def palyazat(request):
    pdfs = PDFDocument.objects.all().order_by('-uploaded_at')  
    return render(request, 'hirek/palyazat.html', {'pdfs': pdfs})


def edzok(request):
    edzok = Edzo.objects.all().order_by('tipus', 'nev')
    return render(request, 'hirek/edzok.html', {'edzok': edzok})
