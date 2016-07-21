"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from django.contrib import admin
import app.views
import settings
import django_twilio.views
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index'),  
    url(r'^index/', 'app.views.index', name='index'),
    url(r'^login/', 'app.views.user_login', name="login"),
    url(r'^signup/', 'app.views.signup', name="signup"),
    url(r'^logout/', 'app.views.user_logout', name="logout"),
    url(r'^showreport/', 'app.views.report', name="report"),
    url(r'^form/', 'app.views.form', name="form"),
    url(r'^market/', 'app.views.marketplace', name="marketplace"),
    url(r'^sms/$', 'app.views.sms', name="sms"),
    url(r'^contact/$', 'app.views.contact', name="contact"),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),     
    url(r'^admin/', include(admin.site.urls)),
    url(r'^message/', 'django_twilio.views.message', {
        'message': 'Yo!',
        'to': '+12535088701',
        'sender': '+12532143686',
        'status_callback': '/message/completed/',
    })
)
