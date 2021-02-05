from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from .models import UrlShort
from django.views import View
from .forms import SubmitURLForm
from analytics.models import ClickEvent
from django.urls import reverse
from UrlShortener import settings


# Create your views here.
def index(request):
    return render(request, 'index.html')


class Create(View):
    def get(self, request, *args, **kwargs):
        form = SubmitURLForm()
        obj = UrlShort.objects.all()
        superuser = False
        if request.user.is_superuser:
            superuser = True
        context = {
            'url': obj,
            'superuser': superuser,
            'form': form
        }
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        obj = UrlShort.objects.all()
        form = SubmitURLForm(request.POST)
        context = {
            'url': obj,
            'form': form
        }
        template = "create.html"
        if form.is_valid():
            url = form.cleaned_data.get("url")
            obj, created = UrlShort.objects.get_or_create(Url=url)
            context = {
                'url': obj,
                'created': created,
            }
            if created:
                template = "success.html"
            else:
                template = "already-exists.html"
        return render(request, template, context)


def url(request, shortcode=None, *args, **kwargs):
    # qs = UrlShort.objects.filter(Short=shortcode)
    # if qs.count() != 1 and not qs.exists():
    #     return Http404
    # obj = qs.first()
    obj = get_object_or_404(UrlShort, Short=shortcode)
    print(ClickEvent.objects.create_event(obj))
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
