from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.show_add),
    url(r'^add$', views.add_to_db),
]