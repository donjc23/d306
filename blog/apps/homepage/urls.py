from django.conf.urls.defaults import *

urlpatterns = patterns('blog.apps.homepage.views',
                       url(r'^$', 'index', name="homepage_index"),
                       url(r'^about/$', 'about', name="homepage_about"),
                       url(r'^contact/$', 'contact', name="homepage_contact"),
                       url(r'^archive/$', 'archive', name="homepage_archive"),
)
