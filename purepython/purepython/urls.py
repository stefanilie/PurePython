from django.conf.urls import patterns, include, url
from fb.views import index
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'purepython.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
)

