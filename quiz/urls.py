from django.conf.urls import url
from .views import index, login_user, logout_user, contact_us, register, enrollment, claim, get_free_quote
from django.urls import path


urlpatterns = [
    url(regex=r'^$', view=index, name='index'),
    url(regex=r'^contact-us/$', view=contact_us, name='contact-us'),
    url(regex=r'^enrollment/$', view=enrollment, name='enrollment'),
    url(regex=r'^get_free_quote/$', view=get_free_quote, name='get_free_quote'),
    url(regex=r'^claim/$', view=claim, name='claim'),
    url(regex=r'^login/$', view=login_user, name='login'),
    url(regex=r'^register/$', view=register, name='register'),
    #url(regex=r'^kid/$', view=kiddos, name='login'),
    url(regex=r'^logout/$', view=logout_user, name='logout'),
    
]