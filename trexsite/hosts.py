from django.conf import settings
from django_hosts import patterns, host
from django.shortcuts import HttpResponseRedirect

def fn(request):
    if 'admin' in request.path:
        request.META['HTTP_HOST'] = "admin.trexengenharia.com.br:8000"
        return HttpResponseRedirect('/admin')

host_patterns =patterns(
    '',

        host(r'www', 'trexsite.hostsconf.trex_urls', name='www'),
        host(r'admin', 'trexsite.hostsconf.admin_urls', callback=fn, name='admin'),
        host(r'blog', 'trexsite.hostsconf.blog_urls', name='blog'),
)