# gabse/urls.py
from django.contrib import admin
from django.urls import path, include
from hirek.views import (
    fooldal, 
    edzok, 
    csapataink, 
    u19, 
    u17, 
    u16, 
    u15, 
    u11, 
    felnott, 
    oregfiuk, 
    oldboys,
    aktualis,
    palyazat,
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Hírekhez kapcsolódó útvonalak
    path('', fooldal, name='fooldal'),
    path('hirek/', include('hirek.urls')),
    
    # Meglévő útvonalak megtartása
    path("index.html", fooldal, name='index'),
    path("edzok.html", edzok, name='edzok'),
    path("csapatok.html", csapataink, name='csapatok'),
    path("csapatok/u19.html", u19, name='u19'),
    path("csapatok/u17.html", u17, name='u17'),
    path("csapatok/u16.html", u16, name='u16'),
    path("csapatok/u15.html", u15, name='u15'),
    path("csapatok/u11.html", u11, name='u11'),
    path("csapatok/felnott.html", felnott, name='felnott'),
    path("csapatok/oldboys.html", oldboys, name='oldboys'),
    path("csapatok/oregfiuk.html", oregfiuk, name='oregfiuk'),
    path("aktualis.html", aktualis, name='aktualis'),
    path('palyazat.html', palyazat, name='palyazat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
