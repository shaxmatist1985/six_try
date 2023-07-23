from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu=[{'title': 'About site', 'url_name': 'about'},
      {'title': 'Add page', 'url_name': 'addpage'},
      {'title': 'Contact', 'url_name': 'contact'},
      {'title': 'Login', 'url_name': 'login'}
      ]

def index(request):
    posts=Man.objects.all()
    context ={
        'posts': posts,
        'menu': menu,
        'title':'main page',
        'cat_selected':0,
    }
    return render(request, 'fifth/index.html', context=context)

def about(request):
    return render(request, 'fifth/about.html', {'menu': menu,'title': 'page about site'})

def addpage(request):
    if request.method == "POST":
        form=AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=AddPostForm()

    return render(request, 'fifth/addpage.html', {'form':form,'menu':menu, 'title':'page for add'})

def contact(request):
    return HttpResponse('<h1>contact</h1>')

def login(request):
    return HttpResponse('<h1>login</h1>')

def show_post(request, post_slug):
    post=get_object_or_404(Man, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'fifth/post.html', context=context)

def show_category(request, cat_id):
    posts = Man.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'main page',
        'cat_selected': cat_id,
    }
    return render(request, 'fifth/index.html', context=context)
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>this page not found</h1>')