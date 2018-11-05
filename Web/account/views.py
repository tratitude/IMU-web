from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from account.models import user_detail
# Create your views here.
def index(request):
	if request.user.is_authenticated:
	   name=request.user.username
	   message="登入成功"
	   return render(request, "index.html", locals())
	else:		
		return redirect("/account/login/")			
		
def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect("/account/index/")			
			else:
				message = '帳號尚未啟用！'
				return render(request, "login.html", locals())
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals())
	
def logout(request):
	auth.logout(request)	
	return redirect('/account/login/')
	message="登出成功"
	
def sign(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		password2 = request.POST['password2']
		mail = request.POST['email']
		user_phone= request.POST['phone']
		if password!=password2:
			message="請輸入相同密碼"
			return render(request,"sign.html",locals())
		try:
			user=User.objects.get(username=name)
		except:
			user=None
		try:
			usermail=User.objects.get(email=mail)
		except:
			usermail=None
		if user!=None :
			message="帳號已有人使用"
			return render(request, "sign.html", locals())
		elif usermail!=None:
			message="信箱已有人使用"
			return render(request, "sign.html", locals())
		else :	
			user=User.objects.create_user(name, mail, password)
			user.is_active=True
			user.save()
			detail=user_detail.objects.create(user=user,phone=user_phone)
			return redirect('/account/login/')
	return render(request, "sign.html", locals())