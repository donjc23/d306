from django.conf.urls.defaults import *
from blog import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

##from django.contrib.staticfiles.urls import staticfiles_urlpatterns
##urlpatterns += staticfiles_urlpatterns()

urlpatterns = patterns('',
    (r'^', include('blog.apps.homepage.urls')),
    (r'^', include('blog.apps.blog_page.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
