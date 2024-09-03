from django.shortcuts import render
import datetime
from .models import Author, Post
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def test(request):
    c_time = datetime.datetime.now().time()
    return render(request, 'test.html', {'c_time':c_time})

def test_url(request, test_param):
    t = str(type(test_param))
    c_time = f"{test_param} {t}"
    return render(request, 'test.html', {'c_time':c_time})

def posts_page(request):
    return HttpResponse("<h1>posts page</h1>")

def post_page(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        return HttpResponseNotFound(f"the post with id {post_id} does not exist")
    return HttpResponse(f"<h1>post page, {p.title}</h1>")

def add_post_page(request):
    return HttpResponse("<h1>add post page</h1>")