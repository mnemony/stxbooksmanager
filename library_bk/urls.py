from django.urls import path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns
 

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('result', views.result, name='result'),
    path('new', views.new, name='new'),
    path('restapi', views.RestBooks.as_view(), name='restapi'),

]