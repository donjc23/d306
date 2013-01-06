from django.conf.urls.defaults import *

urlpatterns = patterns('blog.apps.blog_page.views',
            url(r'^main_blog/$', 'main_blog', name="blog_page_main_blog"),
            url(r'^main_blog/b010613/$', 'b010613', name="blog_page_b010613"),         
            url(r'^main_blog/b010614/$', 'b010614', name="blog_page_b010614"),           
)
