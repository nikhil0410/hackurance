from django.conf.urls import url
from .views import index, login_user, logout_user, contact_us, register
from django.urls import path


urlpatterns = [
    url(regex=r'^$', view=index, name='index'),
    url(regex=r'^contact-us/$', view=contact_us, name='contact-us'),
    url(regex=r'^login/$', view=login_user, name='login'),
    url(regex=r'^register/$', view=register, name='register'),
    #url(regex=r'^kid/$', view=kiddos, name='login'),
    url(regex=r'^logout/$', view=logout_user, name='logout'),
    
]