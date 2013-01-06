# Create your views here.
from django.shortcuts import render_to_response
from blog.apps.data.models import Entry
from django.template import RequestContext

from blog.apps.homepage.forms import ContactForm


def main_blog(request):
    return render_to_response('blog_page/main_blog.html', context_instance=RequestContext(request))


def b010613(request):
    return render_to_response('blog_page/010613.html', context_instance=RequestContext(request))

def b010614(request):
    return render_to_response('blog_page/010614.html', context_instance=RequestContext(request))
