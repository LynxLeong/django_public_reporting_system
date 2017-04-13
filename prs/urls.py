from django.conf.urls import url

from . import views

#app_name = 'prs'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.report, name='report'),
    url(r'report.html', views.report, name='report'),
    url(r'areastatus.html', views.areastatus, name='areastatus'),
    url(r'^register$', views.register, name='register'),
]
