"""jyhoby_com URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
import todolist.urls
from .import views
import products.views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.welcome, name="欢迎页面"),
    path('home', views.home, name="主页"),
    path('admin/', admin.site.urls),
    path('todo/', include(todolist.urls)), #todolist app路由分配

    path('blog/', include('blog.urls')),
    path('product_list/', products.views.product_list, name='产品列表主页'),
    # path('account/', include('account.urls')),
    path('products/', include('products.urls')),

    path('myauth/', include('myauth.urls')), #账户app路由
    path('captcha/', include('captcha.urls')), #短信验证码app路由

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)