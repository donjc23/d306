from django.shortcuts import render_to_response
from blog.apps.data.models import Entry
from django.template import RequestContext

def index(request):
    entries = Entry.objects.published_entries().order_by('-id')
    ctx = {'entries':entries}
    return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
    return render_to_response('homepage/about.html', context_instance=RequestContext(request))

def contact(request):
    return render_to_response('homepage/contact.html', context_instance=RequestContext(request))

def youtube(request):
    return render_to_response('homepage/youtube.html', context_instance=RequestContext(request))
