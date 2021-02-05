from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.Create.as_view(), name = 'create'),
    path('url/delete/<int:id>',views.delete_url, name = 'delete'),
    path('<slug:shortcode>',views.url, name = 'url'),
]