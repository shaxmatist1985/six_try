from django import forms
from fifth.models import *

class AddPostForm(forms.Form):
    title=forms.CharField(max_length=255)
    slug=forms.SlugField(max_length=255)
    content=forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}))
    is_published=forms.BooleanField()
    cat=forms.ModelChoiceField(queryset=Category.objects.all())