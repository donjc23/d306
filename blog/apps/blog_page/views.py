# Create your views here.
from django.shortcuts import render_to_response
from blog.apps.blog_page.models import Comment
from django.template import RequestContext
from django import db

from blog.apps.blog_page.forms import CommentForm


def main_blog(request):
    success = False
    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            success = True
            comment_form.save()
            db.close_connection()
            
    else:
        comment_form = CommentForm()

    entries = Comment.objects.filter(published=True).order_by('-id')
    db.close_connection()
    ctx = {'comment_form':comment_form, 'entries':entries,'success':success }
    return render_to_response('blog_page/main_blog.html',ctx, context_instance=RequestContext(request))


def b010613(request):
    return render_to_response('blog_page/010613.html', context_instance=RequestContext(request))

def b010614(request):
    return render_to_response('blog_page/010614.html', context_instance=RequestContext(request))
