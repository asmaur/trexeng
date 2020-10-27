from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticSitemap(Sitemap):

    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ["sobre", "ppci", "obras", "laudos", "reformas", "estruturas",  "contato"]

    def location(self, item):
        return reverse(item)