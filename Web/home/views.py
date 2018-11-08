from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
 
# 首頁
<<<<<<< HEAD
def home(request):#顯示三篇最近訊息
    articalall=models.artical_model.objects.all().order_by("-artical_add_date")
    if len(articalall)>=1:
        artical_first=articalall[0]
    if len(articalall)>=2:
        artical_second=articalall[1]
    if len(articalall)>=3:
        artical_third=articalall[2]
=======
def home(request):
    articalall=models.artical_model.objects.all().order_by("-artical_add_data")
>>>>>>> 10ca378b96dadcbc89af91458e5a2a94c3af6fd3
    return render(request, "home/home.html", locals())
	
# 布告欄
def Bulletin(request):
    if request.method == 'POST':
        if request.POST['type']!='all':
            type=request.POST['type']
            articalall=models.artical_model.objects.filter(artical_type=type)
        if request.POST['keyword']!='':
            keyword=request.POST['keyword']
            articalall=models.artical_model.objects.filter(artical_title__icontains=keyword)
        if request.POST['keyword']!='' or request.POST['type']!='all' :
<<<<<<< HEAD
            articalall=articalall.order_by("-artical_add_date")
        else:
            articalall=models.artical_model.objects.all().order_by("-artical_add_date")
    else :
        articalall=models.artical_model.objects.all().order_by("-artical_add_date")
=======
            articalall=articalall.order_by("-artical_add_data")
        else:
            articalall=models.artical_model.objects.all().order_by("-artical_add_data")
    else :
        articalall=models.artical_model.objects.all().order_by("-artical_add_data")
>>>>>>> 10ca378b96dadcbc89af91458e5a2a94c3af6fd3
    return render(request, "home/Bulletin.html", locals())

	
#公告顯示
def artical(request,artical=None):
    artical = models.artical_model.objects.get(id=artical)
    return render(request, "home/artical.html", locals())


#文章輸入
def input_artical(request):
    if request.method == 'POST':
        artical=models.artical_model()
        artical.artical_title=request.POST['title']
        artical.artical_type = request.POST['type']
        artical.artical_content = request.POST['content']
        artical.save()
        return redirect('/home/artical/'+str(artical.id))
    return render(request, "home/input_artical.html", locals())

def search_artical(request,type='',keyword=None):
    type=type+'_icontains'
<<<<<<< HEAD
    articalall=models.artical_model.objects.filter(type=keyword).order_by("-artical_add_date")
=======
    articalall=models.artical_model.objects.filter(type=keyword).order_by("-artical_add_data")
>>>>>>> 10ca378b96dadcbc89af91458e5a2a94c3af6fd3
    return render(request, "home/Bulletin.html", locals())
	
#文章刪除
def delete_artical(request,artical=None):
    if artical != 'None':
        artical_in_database=models.artical_model.objects.get(id=artical)
        artical_in_database.delete()
    return redirect("/home/Bulletin")
<<<<<<< HEAD

#文章修改
def update_artical(request,artical=None):
    artical_model=models.artical_model.objects.get(id=artical)
    if request.method == 'POST':
        artical_model.artical_title=request.POST['title']
        artical_model.artical_content = request.POST['content']
        artical_model.save()
        return redirect('/home/artical/'+str(artical_model.id))
    return render(request, "home/update_artical.html", locals())
=======
>>>>>>> 10ca378b96dadcbc89af91458e5a2a94c3af6fd3
	
