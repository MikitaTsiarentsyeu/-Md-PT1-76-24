"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts/', main_views.PostsView.as_view(), name="posts_page"),
    path('posts/<int:post_id>/', main_views.PostView.as_view(), name="post_page"),
    path('posts/add/', main_views.AddPostView.as_view(), name="add_post_page"),
    # path('test/<str:test_param>/', main_views.test_url),
    # path('test/<int:test_param>/', main_views.test_url),
    path('admin/', admin.site.urls),
]

urlpatterns += [path('accounts/', include('django.contrib.auth.urls')),]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
