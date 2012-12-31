from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'blog.apps.homepage.views.index'),
)
