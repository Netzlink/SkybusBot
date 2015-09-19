from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'telegram', hello.views.telegram_callback, name='telegram_callback'),
    url(r'update_location', hello.views.update_location, name='update_location'),
    url(r'^admin/', include(admin.site.urls)),

)
