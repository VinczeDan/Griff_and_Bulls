# gabse/urls.py
from django.contrib import admin
from django.urls import path, include
from hirek.views import (
    fooldal, 
    edzok, 
    csapataink, 
    korosztaly,
    aktualis,
    palyazat,
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', fooldal, name='fooldal'),
    path('hirek/', include('hirek.urls')),
    path("index/", fooldal, name='index'),
    path('edzok/', edzok, name='edzok'),
    path("csapatok/", csapataink, name='csapatok'),
    path("csapatok/korosztaly/<slug:korosztaly_slug>/", korosztaly, name='korosztaly'),
    path("aktualis/", aktualis, name='aktualis'),
    path('palyazat/', palyazat, name='palyazat'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
