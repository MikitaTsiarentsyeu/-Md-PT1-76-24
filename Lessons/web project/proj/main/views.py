from django.shortcuts import render, redirect
import datetime
from .models import Author, Post
from django.http import HttpResponse, HttpResponseNotFound
from .forms import AddPostForm, AddPostModelForm
from django.contrib.auth.decorators import permission_required
from django.views import View

# Create your views here.
# def test(request):
#     c_time = datetime.datetime.now().time()
#     return render(request, 'test.html', {'c_time':c_time})

# def test_url(request, test_param):
#     t = str(type(test_param))
#     c_time = f"{test_param} {t}"
#     return render(request, 'test.html', {'c_time':c_time})

class PostModelViewBase:

    model = Post

    def get_all_posts(self):
        return self.model.objects.all()
    
    def get_post(self, post_id):
        try:
            p = self.model.objects.get(id=post_id)
            return p
        except:
            return False
        
    def add_post(self, form, author):
        post_entry = form.save(commit=False)
        post_entry.author = author
        post_entry.issued = datetime.datetime.now()

        form.save()
        form.save_m2m()

        return post_entry.id

class SessionViewBase:

    session_key = 'vp'

    def get_post_ids(self, request):
        return request.session.get(self.session_key, [])
    
    def set_post_id(self, request, id):
        vp = self.get_post_ids()
        if id not in vp:
            vp.append(id)
        request.session[self.session_key] = vp



class PostsView(View, PostModelViewBase, SessionViewBase):

    template = 'posts_page.html'

    def get(self, request):
        posts = self.get_all_posts()
        vp = self.get_post_ids(request)
        return render(request, self.template, {'posts_obj':posts, 'vp': vp})


class PostView(View, PostModelViewBase, SessionViewBase):

    template = 'post_page.html'

    def get(self, request, post_id):
        post = self.get_post(post_id)
        if post:
            vp = self.get_post_ids(request)
            if post.id not in vp:
                self.set_post_id(post.id)
            return render(request, 'post_page.html', {'post_obj':post})
        else:
            return HttpResponseNotFound(f"the post with id {post_id} does not exist")



class AddPostView(View, PostModelViewBase):

    # form = AddPostModelForm

    def post(self, request):
        form = AddPostModelForm(request.POST, request.FILES)

        if form.is_valid():

            post_entry = self.add_post(form, Author.objects.get(email=request.user.email))

            return redirect('post_page', post_entry.id)

    def get(self, request):
        form = AddPostModelForm()
        return render(request, 'add_post_page.html', {'form':form})










# def posts_page(request):
#     posts = Post.objects.all()
#     vp = request.session.get('vp', [])
#     return render(request, 'posts_page.html', {'posts_obj':posts, 'vp': vp})

# def post_page(request, post_id):
#     try:
#         p = Post.objects.get(id=post_id)
#         vp = request.session.get('vp', [])
#         if p.id not in vp:
#             vp.append(p.id)
#         request.session['vp'] = vp
#     except:
#         return HttpResponseNotFound(f"the post with id {post_id} does not exist")
#     return render(request, 'post_page.html', {'post_obj':p})


# def add_post_page(request):

#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)

#         if form.is_valid():
#             post_entry = Post()
#             post_entry.author = Author.objects.all()[0] #temporary solution
#             post_entry.issued = datetime.datetime.now()
#             post_entry.title = form.cleaned_data['title']
#             post_entry.content = form.cleaned_data['content']
#             post_entry.post_type = form.cleaned_data['post_type']
#             post_entry.image = form.cleaned_data['image']
#             post_entry.save()

#             return redirect('post_page', post_entry.id)

#     else:
#         form = AddPostForm()

#     return render(request, 'add_post_page.html', {'form':form})

# @permission_required("main.add_post")
# def add_post_page(request):

#     if request.method == 'POST':
#         form = AddPostModelForm(request.POST, request.FILES)

#         if form.is_valid():
#             post_entry = form.save(commit=False)
#             post_entry.author = Author.objects.get(email=request.user.email)
#             post_entry.issued = datetime.datetime.now()

#             # post_entry.save()
#             form.save()
#             form.save_m2m()

#             return redirect('post_page', post_entry.id)

#     else:
#         form = AddPostModelForm()

#     return render(request, 'add_post_page.html', {'form':form})

# Docker

# Postgre, MongoDB, apache kafka or rabbitMQ, (elasticsearch, reddis, solr)

# JavaScript or TypeScript, React or Angular or Vue or Svelta, (node.js)