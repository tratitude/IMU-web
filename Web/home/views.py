from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
 
# 首頁
def home(request):
    articalall=models.artical_model.objects.all().order_by("-artical_add_data")
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
            articalall=articalall.order_by("-artical_add_data")
        else:
            articalall=models.artical_model.objects.all().order_by("-artical_add_data")
    else :
        articalall=models.artical_model.objects.all().order_by("-artical_add_data")
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
    articalall=models.artical_model.objects.filter(type=keyword).order_by("-artical_add_data")
    return render(request, "home/Bulletin.html", locals())
	
#文章刪除
def delete_artical(request,artical=None):
    if artical != 'None':
        artical_in_database=models.artical_model.objects.get(id=artical)
        artical_in_database.delete()
    return redirect("/home/Bulletin")
	
