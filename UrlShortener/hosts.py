from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'ngsu', settings.ROOT_URLCONF, name='ngsu'),
    host(r'(?!www).*', 'UrlShortener.hostconf.urls', name='wildcard'),
)
