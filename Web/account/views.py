from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from account.models import user_detail
# username -> user內建的帳號名 		拿來當作帳號使用
# firstname -> user內建的first_name	拿來當作用戶姓名使用
def index(request):
	if request.user.is_authenticated:
	   name=request.user.first_name
	   message="登入成功"
	   return render(request, "account/index.html", locals())
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
				return render(request, "account/login.html", locals())
		else:
			message = '登入失敗！'
	return render(request, "account/login.html", locals())
	
def logout(request):
	auth.logout(request)	
	return redirect('/account/login/')
	message="登出成功"

def modify(request):
	if not request.user.is_authenticated:		#確認登入狀態
		return redirect("/account/login/")
	user=request.user
	detail=user_detail.objects.get(user=user)
	username=user.username
	name=user.first_name
	phone=user_detail.objects.get(user=user).phone
	mail=user.email
	if request.method == 'POST':				#收表單修改
		newname=request.POST['firstname']
		newphone=request.POST['phone']
		newmail=request.POST['email']
		if name!=newname:
			user.first_name=newname
			user.save()
		if phone!=newphone:		
			detail.phone=newphone
			detail.save()
		if mail!=newmail:
			user.email=newmail
			user.save()
		return redirect("/account/index/")
	else:		
		return render(request,"account/modify.html",locals())

def modify_password(request):
	if not request.user.is_authenticated:		#確認登入狀態
		return redirect("/account/login/")
	user=request.user
	username=user.username
	if request.method == 'POST':				#收表單修改
		curpass=request.POST['current_pass']
		npass=request.POST['new_pass']	
		chpass=request.POST['check_pass']
		if not user.check_password(curpass):					
			message="當前密碼錯誤"
			return render(request,"account/modify_password.html",locals())
		if npass!=chpass:
			message="新密碼不符"
			return render(request,"account/modify_password.html",locals())
		user.set_password(npass)
		user.save()
		User = authenticate(username=username, password=npass)	#直接重新登入
		auth.login(request,User)
		return redirect("/account/index/")
	else :
		return render(request,"account/modify_password.html",locals())
		
def sign(request):
	if request.method == 'POST':
		name=request.POST['username']
		firstname = request.POST['firstname']
		password = request.POST['password']
		password2 = request.POST['password2']
		mail = request.POST['email']
		user_phone= request.POST['phone']
		if password!=password2:
			message="請輸入相同密碼"
			return render(request,"account/sign.html",locals())
		try:	#帳號是否重複使用
			User.objects.get(username=name)
			message="帳號已有人使用"
			return render(request, "account/sign.html", locals())			
		except:
			pass
		try:	#信箱是否重複使用
			User.objects.get(email=mail)
			message="信箱已有人使用"
			return render(request, "account/sign.html", locals())
		except:
			pass
		user=User.objects.create_user(name, mail, password,first_name=firstname)
		user.is_active=True		#信箱認證會用到 還沒做
		user.save()
		detail=user_detail.objects.create(user=user,phone=user_phone)
		return redirect('/account/login/')
	return render(request, "account/sign.html", locals())