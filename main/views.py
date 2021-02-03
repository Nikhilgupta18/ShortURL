from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import UrlShort
from django.views import View
from django.urls import reverse
from UrlShortener import settings
# Create your views here.


class Home(View):
    def get(self, request, *args, **kwargs):
        obj = UrlShort.objects.all()
        superuser = False
        if request.user.is_superuser:
            superuser = True
        context = {
            'url': obj,
            'superuser': superuser
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        # print(request.POST.get("url"))
        obj = UrlShort.objects.all()
        print(obj)
        # obj.save()
        context = {
            'url': obj
        }
        return render(request, 'index.html', context)


def url(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(UrlShort, Short=shortcode)
    # this is best method as it return 404 error when not found, which is good for url not found
    return HttpResponseRedirect(obj.Url)

    # print(request.user)
    # print(shortcode)
    # obj = UrlShort.objects.get(Short=shortcode)
    # this does not handle the query which does not exists and raise an exception.
    # try method prints the query which are present and for does not exists we can do anything we want
    # try:
    #     obj = UrlShort.objects.get(Short=shortcode)
    #
    # except:
    #     obj = UrlShort.objects.first() #returning first object in all objects in the table
    # context = {
    #     'shortcode': obj.Url,
    # }
    # return render(request, 'index.html', context)


def delete_url(request, id):
    if request.method == 'POST':
        print(request.POST)
        obj = UrlShort.objects.get(id=id)
        obj.delete()
        return redirect('index')
    obj = UrlShort.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, 'delete.html', context)

