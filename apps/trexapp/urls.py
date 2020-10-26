from django.urls import include, re_path, path

from .views import *



urlpatterns = [
    re_path(r'^$',index, name='home'),
    re_path(r'^sobre-nos$',sobre),
    re_path(r'^contato/$',contato),
    re_path(r'^ppci$',ppci),
    re_path(r'^laudos-tecnicos$',laudos),
    re_path(r'^execucao-de-obra$',obras),
    re_path(r'^projeto-de-estruturas$', estruturas),
    re_path(r'^reformas-em-geral$', reformas),
    re_path(r'^sitemap$', sitemap),
]