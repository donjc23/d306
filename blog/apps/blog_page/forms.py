from django import forms
from blog.apps.blog_page.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
