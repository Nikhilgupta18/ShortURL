from django.db import models

from .utils import code_generator, create_shortcode
from .validators import validate_url

from django_hosts.resolvers import reverse


class UrlShortManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(UrlShortManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs


class UrlShort(models.Model):
    Url = models.CharField(max_length=200, validators=[validate_url])
    Short = models.CharField(max_length=15, unique=True, blank=True)
    Updated = models.DateTimeField(auto_now=True)
    Time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = UrlShortManager()  # overrides the inbuilt 'objects 'manager with UrlShortManager's objects
    # some_random_name = UrlShortManager() #this also works like- UrlShort.some_random_name.all(),
    # this is our own manager name ie we can create our own model manager

    def save(self, *args, **kwargs):
        if not self.Short:
            self.Short = create_shortcode(self)
        if not "http" in self.Url:
            self.Url = "http://" + self.Url
        super(UrlShort, self).save(*args, **kwargs)

    def __str__(self):
        return self.Url

    def get_short_url(self):
        url_path = reverse("url", kwargs={'shortcode': self.Short}, host='www', scheme='http')
        return url_path

