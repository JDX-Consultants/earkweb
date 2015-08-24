from django.conf.urls import patterns, url

from sip2aip import views

from earkcore.views import InformationPackageDetailView

urlpatterns= patterns('',

    url(r'^$', views.InformationPackageList.as_view(),name='reception'),

    url(r'^detail/(?P<pk>\d+)/$', views.InformationPackageDetail.as_view(), name='ip_detail'),

    url(r'^progress$', views.progress, name='progress'),

    url(r'^apply_task', views.apply_task, name='apply_task'),

    url(r'^poll_state$', views.poll_state, name='poll_state'),

    url(r'^ip_detail_table$', views.ip_detail_table, name='ip_detail_table'),

    url(r'^working_area/(?P<uuid>[a-z0-9-]{36,36})/$', views.working_area, name='working_area'),

    url(r'^get_directory_json$', views.get_directory_json, name='get_directory_json'),

)