# -*- coding: cp936 -*-
from django.shortcuts import render_to_response
from blog.apps.data.models import Entry
from django.template import RequestContext

from blog.apps.homepage.forms import ContactForm

def index(request):
    entries = Entry.objects.published_entries().order_by('-id')
    ctx = {'entries':entries}
    return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))

def about(request):
    return render_to_response('homepage/about.html', context_instance=RequestContext(request))

def contact(request):
    success = False
    email = ''
    title = ''
    text = ''
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            text = contact_form.cleaned_data['text']
    else:
        contact_form = ContactForm()

    ctx = {'contact_form':contact_form, 'email':email, 'text':text, 'title':title, 'success':success}
    
    return render_to_response('homepage/contact.html', ctx, context_instance=RequestContext(request))

def youtube(request):
    success = True
    videos =[
	{"video": {"caption":"PSY - GANGNAM STYLE ", "source":"http://www.youtube.com/embed/9bZkp7q19f0"} },
	{"video": {"caption":"Justin Bieber - Baby ft. Ludacris", "source":"http://www.youtube.com/embed/kffacxfA7G4"} },
	{"video": {"caption":"Jennifer Lopez - On The Floor ft. Pitbull", "source":"http://www.youtube.com/embed/t4H_Zoh7G5A"} },
	{"video": {"caption":"Eminem - Love The Way You Lie ft. Rihanna", "source":"http://www.youtube.com/embed/uelHwf8o7_U"} },
	{"video": {"caption":"LMFAO - Party Rock Anthem ft. Lauren Bennett, GoonRock", "source":"http://www.youtube.com/embed/KQ6zr6kCPj8"} },
	{"video": {"caption":"Waka Waka (This Time for Africa)", "source":"http://www.youtube.com/embed/pRpeEdMmmQ0"} },
	{"video": {"caption":"Lady Gaga - Bad Romance", "source":"http://www.youtube.com/embed/qrO4YZeyl0I"} },
	{"video": {"caption":"Michel - Ai Se Eu Te Pego", "source":"http://www.youtube.com/embed/hcm55lU9knw"} },
	{"video": {"caption":"Don Omar - Danza Kuduro ft. Lucenzo", "source":"http://www.youtube.com/embed/7zp1TbLFPp8"} },
	{"video": {"caption":"Eminem - Not Afraid", "source":"http://www.youtube.com/embed/j5-yKhDd64s"} }
    ]
    ctx = {'videos':videos, 'success':success}
    return render_to_response('homepage/youtube.html', ctx, context_instance=RequestContext(request))

def csrf_rejected(request, reason=""):
    ctx = {'reason':reason}
    return render_to_response('homepage/rejected.html', ctx, context_instance=RequestContext(request))

