from django.urls import include, re_path, path
from .views import *



urlpatterns = [
    re_path(r'^$',blog),
    re_path(r'^contato/$',contato),
    re_path(r'^projetos/(?P<code>\d+)/(?P<slug>[\w-]+)/$',detail),

]
