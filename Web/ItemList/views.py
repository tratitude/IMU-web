from django.shortcuts import render
from datetime import datetime
from ItemList.models import Item

def list(request):
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

