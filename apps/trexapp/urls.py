from django.urls import re_path
from .sitemaps import StaticSitemap
from django.contrib.sitemaps.views import sitemap

from . import views

sitemaps = {
    'static': StaticSitemap(),
}


urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^sobre-nos$', views.sobre, name='sobre'),
    re_path(r'^contato$', views.contato, name="contato"),
    re_path(r'^ppci$', views.ppci, name="ppci"),
    re_path(r'^laudos-tecnicos$', views.laudos, name="laudos"),
    re_path(r'^execucao-de-obra$', views.obras, name="obras"),
    re_path(r'^projeto-de-estruturas$', views.estruturas, name="estruturas"),
    re_path(r'^reformas-em-geral$', views.reformas, name="reformas"),
    re_path(r'^sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]