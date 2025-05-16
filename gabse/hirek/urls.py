# hirek/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fooldal, name='fooldal'),
    path('hirek/', views.hirek_oldal, name='hirek_oldal'),
    path('hirek/<slug:slug>/', views.hir_reszletek, name='hir_reszletek'),
    path('aktualis/', views.aktualis, name='aktualis'),
]