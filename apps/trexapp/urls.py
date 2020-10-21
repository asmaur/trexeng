from django.urls import include, re_path, path

from .views import *



urlpatterns = [
    re_path(r'^$',index, name='home'),
    re_path(r'^sobre-nos$',sobre),
    re_path(r'^contato/$',contato),
    re_path(r'^ppci$',ppci),
    re_path(r'^laudos$',laudos),
    re_path(r'^obras$',obras),
    re_path(r'^estruturas$', estruturas),
    re_path(r'^reformas$', reformas),
]