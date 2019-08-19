from django.urls import include, re_path, path

from .views import *



urlpatterns = [
    re_path(r'^$',index, name='home'),
    re_path(r'^sobre-nos$',sobre),
    re_path(r'^contato/$',contato),
    re_path(r'^projetos/ppci$',ppci),
    #re_path(r'^projetos/eletricos$', eletricos),
    re_path(r'^projetos/estruturas$', estruturas),
    #re_path(r'^projetos/bim-3d', bim_3d),
    #re_path(r'^projetos/hidro-sanitarios$', hidro_sanitarios),
    re_path(r'^projetos/reformas$', reformas),
    #re_path(r'^projetos/blog$', blog),
    #re_path(r'^projetos/blog/titre$', detail),
]