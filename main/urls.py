from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home.as_view(), name = 'index'),
    path('url/delete/<int:id>',views.delete_url, name = 'delete'),
    path('url/<slug:shortcode>',views.url, name = 'url'),
#     path('url/delete/<int:id>',delete_url_id, name = 'delete_url'),
]