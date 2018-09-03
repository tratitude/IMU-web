from django.shortcuts import get_object_or_404, render
from datetime import datetime
from ItemList.models import Item,ItemTag
from django.core.paginator import Paginator
def pd(request,Identity):
        Id = get_object_or_404(Item, Identity=Identity)
        return render(request, 'ItemList/Detail.html', {'Id': Id})

def listfor(request,ord):
    tag = request.session['t']
    ORD = "Name"
    if(request.session['ORD']==ord):
        ORD="-"+ord
    elif(ord=="Name"):ORD="Name"
    elif(ord=="price"):ORD= "price"
    elif (ord == "created_at"):ORD= "created_at"
    else:
        tag = ItemTag.objects.get(Tag=ord)
        request.session['t'] = tag
    ItemTags = ItemTag.objects.all()
    request.session['ORD'] = ORD
    if  request.session['fil']!=None:
        Name = request.session['fil']
        if(tag==None):
            Items = Item.objects.filter(Name__icontains=Name).order_by(ORD)
        else:
            Items = tag.items.filter(Name__icontains=Name).order_by(ORD)
        if  not Items:
            return render(request, 'ItemList/None.html',locals())
    else:
        if(tag==None):
            Items = Item.objects.all().order_by(ORD)
        else:
            Items = tag.items.all().order_by(ORD)
    paginator = Paginator(Items,5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'ItemList/home.html',locals())
def list(request):
    #Ord = request.POST['order']
    request.session['t']=None
    request.session['ORD']=None
    ItemTags = ItemTag.objects.all()
    if  'ok' in request.POST:
        Name = request.POST['Name']
        request.session['fil'] = Name
        Items = Item.objects.filter(Name__icontains=Name).order_by('-Name')
        if not Items:
            return render(request, 'ItemList/None.html',locals())
    else:
        request.session['fil'] = None
        Items = Item.objects.all().order_by('-Name')
        mycontext = {
         'current_time': str(datetime.now())
        }
    paginator = Paginator(Items, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'ItemList/home.html', locals())

def listone(request):
    try:
        unit = Item.objects.get(Name="智慧型手機")
    except:
        errormessage = "讀取錯誤"
    return render(request,'ItemList/listone.html',locals())

def upload(request):
    if request.method =='POST':
        img = Item(photo=request.FILES.get('img'))
        img.save()
    return render(request,'ItemList/imgUpload.html')

def show(request):
    Items = Item.objects.all()
    context = {
        'Items'  :   Items
    }
    return render(request,'ItemList/Detail.html',context)
