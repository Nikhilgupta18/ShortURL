from django.db import models
from main.models import UrlShort
# Create your models here.


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, UrlShort):
            obj, created = self.get_or_create(url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    url = models.OneToOneField(UrlShort, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{url} : {i}".format(url=self.url, i=self.count)
