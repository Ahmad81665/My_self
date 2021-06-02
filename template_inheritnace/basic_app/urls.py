from django.conf.urls import url

from basic_app import views


app_name = 'basic_app'



urlpatterns = [
    url(r'^relative/$', views.relative,name='relative'),
    url(r'^about/$', views.about,name='about'),
    url(r'^projects/$', views.projects,name='projects'),
    url(r'^skills/$', views.skills,name='skills'),
    url(r'^contact/$', views.contact,name='contact'),
    
]