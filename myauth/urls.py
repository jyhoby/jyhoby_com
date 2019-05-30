from django.urls import path
from .import views
app_name='myauth'

urlpatterns = [
    path('', views.home,name='主页'),
    path('login/', views.denglu,name='登录'),
    path('logout/', views.dengchu,name='登出'),
    path('register/', views.zhuce,name='注册'),
    path('user_center/', views.个人中心,name='个人中心'),
    path('user_center/edit_profile', views.编辑个人信息,name='编辑个人信息'),
    path('user_center/change_password', views.修改密码,name='修改密码'),
    path('user_center/sms', views.短信验证码,name='短信验证码'),




]
