from django.shortcuts import render
from datetime import datetime
from ItemList.models import Item

def list(request):
    if  'ok' in request.POST:
        Name = request.POST['Name']
        Items = Item.objects.filter(Name__icontains=Name)
        return render(request, 'ItemList/home.html',locals())
    else:
        Items = Item.objects.all().order_by('-Name')
        mycontext = {
         'current_time': str(datetime.now())
        }
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
    return render(request,'ItemList/show.html',context)
