from django.urls import re_path, include
from Agenda import views

urlpatterns = [
    re_path(r'^$', views.pessoa_list, name='pessoa_list'),
    re_path(r'^new$', views.pessoa_create, name='pessoa_new'),
    re_path(r'^delete/(?P<id>\d+)$', views.pessoa_delete, name='pessoa_delete'),
    re_path(r'^edit/(?P<id>\d+)$', views.edit_pessoa, name='edit_pessoa'),
]
