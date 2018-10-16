from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.register),
    url(r'^wand$', views.add_wand),
    url(r'^\d+$', views.show_wizard),
]