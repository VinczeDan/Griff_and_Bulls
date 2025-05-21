# gabse/urls.py
from django.contrib import admin
from django.urls import path, include
from hirek.views import (
    fooldal, 
    edzok, 
    csapataink, 
    korosztaly,
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
    path("index/", fooldal, name='index'),
    path("edzok/", edzok, name='edzok'),
    path("csapatok/", csapataink, name='csapatok'),
    path("csapatok/korosztaly/<slug:korosztaly_slug>/", korosztaly, name='korosztaly'),
    path("csapatok/felnott", felnott, name='felnott'),
    path("csapatok/oldboys/", oldboys, name='oldboys'),
    path("csapatok/oregfiuk/", oregfiuk, name='oregfiuk'),
    path("aktualis/", aktualis, name='aktualis'),
    path('palyazat/', palyazat, name='palyazat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
