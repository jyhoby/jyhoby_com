from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm,AuthenticationForm
from .forms import 自定义注册表单, 自定义编辑表单
from .forms import 自定义登录表单
# from django.contrib import auth
from django.contrib.auth.models import User
from .models import 普通会员表
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from random import randint
import time
from .mypage.my_re import isUserName, isPassWord #导入自定义的正则

#from .demo_sms_send import send_sms
#params = u'{"code":"%d"}' % randint(100000,999999)
# send_sms(str(request.普通会员表.手机号码),params)




# Create your views here.
@login_required(login_url='myauth:登录')
def 个人中心(request):
	内容 = {'用户': request.user}
	return render(request,'myauth/user_center.html',内容)

@login_required(login_url='myauth:登录')
def 编辑个人信息(request):
	if request.method=='POST':
		编辑表单=自定义编辑表单(request.POST,instance=request.user)
		if 编辑表单.is_valid():
			编辑表单.save()
			request.user.普通会员表.昵称=编辑表单.cleaned_data['昵称']
			request.user.普通会员表.生日=编辑表单.cleaned_data['生日']
			request.user.普通会员表.save()
			# user=authenticate(username=注册表单.cleaned_data['username'],password=注册表单.cleaned_data['password1'])
			return redirect("myauth:个人中心")

	else:
		编辑表单=自定义编辑表单(instance=request.user)

	content={'编辑表单':编辑表单,'用户':request.user}
	return render(request,"myauth/edit_profile.html",content)

@login_required(login_url='myauth:登录')
def 短信验证码(request):
	if request.method=='POST':
		if time.time()>request.session.get('重新发送时间',0):
			验证码=randint(100000,999999)
			# request.session['验证码'] = 验证码
			request.session['验证码'] =验证码
			request.session['重新发送时间'] = time.time()+60
			request.session['超时时间'] = time.time()+120
			#params = u'{"code":"%d"}' %验证码
			#send_sms('18406661217',template_param=params)
			print(验证码,'已发送')
			messages.success(request,验证码)
			# messages.success(request,'验证码发送成功')
			return redirect("myauth:修改密码")
		else:
			messages.success(request,'验证码发送时间间隔为60秒')
			return redirect("myauth:修改密码")
	else:
		return redirect("myauth:修改密码")

@login_required(login_url='myauth:登录')
def 修改密码(request):

	# 验证码错误=''
	# if request.method=='POST':
	# 	改密表单=PasswordChangeForm(data=request.POST,user=request.user)
	# 	if not request.session.get('验证码'):
	# 		验证码错误='请先点击发送验证码按钮'
	# 	elif time.time() > request.session['超时时间']:
	# 		验证码错误='验证码超时'
	# 	elif request.POST['验证码'] !=str(request.session['验证码']):
	# 		验证码错误='验证码错误'
	# 	elif 改密表单.is_valid():
	# 		改密表单.save()
	# 		# user=authenticate(username=注册表单.cleaned_data['username'],password=注册表单.cleaned_data['password1'])
	# 		return redirect("myauth:登录")

	# else:
	# 	改密表单=PasswordChangeForm(user=request.user)

	# # content={'改密表单':改密表单,'用户':request.user,'验证码错误':验证码错误}
	content={'改密表单':改密表单,'用户':request.user}
	return render(request,"myauth/change_password.html",content)

def home(request):
	return render(request,'myauth/home.html')


def denglu(request):
	if request.method=="POST":
		登录表单 =自定义登录表单(data=request.POST)
		if 登录表单.is_valid():
			user = authenticate(request, username=登录表单.cleaned_data['username'], password=登录表单.cleaned_data['password'] )
			login(request,user)
			# return redirect("myauth:主页")
			return redirect("主页")
	else:
		if request.user.is_authenticated:
			# return redirect("myauth:主页")
			return redirect("主页")
		else:
			登录表单=自定义登录表单()
		
	content={'登录表单':登录表单,'用户':request.user}
	return render(request,'myauth/login.html',content)


def dengchu(request):
	logout(request)
	return redirect("主页")


def zhuce(request):
	if request.method=='POST':
		username=request.POST["username"]
		if isUserName(username):
			password=request.POST["password1"]
			if isPassWord(password):
				注册表单=自定义注册表单(request.POST)
				if 注册表单.is_valid():
					注册表单.save()
					user=authenticate(username=注册表单.cleaned_data['username'],password=注册表单.cleaned_data['password1'])
					user.email = 注册表单.cleaned_data['email']
					普通会员表(用户=user,昵称=注册表单.cleaned_data['昵称'],生日=注册表单.cleaned_data['生日']).save()
					login(request,user)
					return redirect("主页")
			else:
				return render(request,"myauth/register.html",{"密码格式错误":"密码格式错误"})
		else:
			return render(request,"myauth/register.html",{"用户名格式错误":"用户名格式错误"})


	else:
		注册表单=自定义注册表单()

	content={'注册表单':注册表单}
	return render(request,"myauth/register.html",content)
	