"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from mysite import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),  # 關於頁面
    path('pricing/', views.pricing, name='pricing'),  # 價錢諮詢
    path('service/', views.service, name='service'),  #
    path('project/', views.project, name='project'),  # project
    path('blog_grid/', views.blog_grid, name='blog_grid'),  #
    path('blog_sidebar/', views.blog_sidebar, name='blog_sidebar'),  #
    path('blog_single/', views.blog_single, name='blog_single'),  #
    path('contact/', views.contact, name='contact'),  #



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

