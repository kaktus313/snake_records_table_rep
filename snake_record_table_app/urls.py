from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^record_list', views.record_list),
    url(r'^send_record', views.send_record)
]