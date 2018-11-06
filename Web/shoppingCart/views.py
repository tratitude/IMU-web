from django.shortcuts import render, redirect
from . import models
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.text import MIMEText
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

message = ''
cartlist = [] # 購買商品串列
shippingFee = 0 # 運費
customname = '' # 購買者姓名
customphone = '' # 購買者電話
customaddress = '' # 購買者地址
customemail = '' # 購買者電子郵件

def index(request):
    global cartlist
    if 'cartlist' in request.session: # 若session中存在cartlist就讀出
        cartlist = request.session['cartlist']
    else: # 重新購物
        cartlist = []
    cartnum = len(cartlist) # 購買商品筆數
    productall = models.ProductModel.objects.all() # 取得資料庫所有商品
    return render(request, "shoppingCart/index.html", locals())

def detail(request, productid=None):
    product = models.ProductModel.objects.get(id=productid) #取得商品
    return render(request, "shoppingCart/detail.html", locals())

def cart(request):  # 顯示購物車
    global cartlist
    global shippingFee
    cartlist1 = cartlist  # 以區域變數模
    shippingFee1 = shippingFee
    total = 0
    for unit in cartlist:  # 計算商品總金額
        total += int(unit[3])
    grandtotal = total + shippingFee  # 加上總費總額
    return render(request, "shoppingCart/cart.html", locals())

def addtocart(request, ctype=None, productid=None):
    global cartlist
    if ctype == 'add':  #加入購物車
        product = models.ProductModel.objects.get(id=productid)
        flag = True  #設檢查旗標為True
        for unit in cartlist:  #逐筆檢查商品是否已存在
            if product.pname == unit[0]:  #商品已存在
                unit[2] = str(int(unit[2])+ 1)  #數量加1
                unit[3] = str(int(unit[3]) + product.pprice)  #計算價錢
                flag = False  #設檢查旗標為False
                break
        if flag:  #商品不存在
            temlist = []  #暫時串列
            temlist.append(product.pname)  #將商品資料加入暫時串列
            temlist.append(str(product.pprice))  #商品價格
            temlist.append('1')  #先暫訂數量為1
            temlist.append(str(product.pprice))  #總價
            cartlist.append(temlist)  #將暫時串列加入購物車
        request.session['cartlist'] = cartlist  #購物車寫入session
        return redirect('/shoppingCart/cart/')
    elif ctype == 'update':  #更新購物車
        n = 0
        for unit in cartlist:
            unit[2] = request.POST.get('qty' + str(n), '1')  #取得數量
            unit[3] = str(int(unit[1]) * int(unit[2]))  #取得總價
            n += 1
        request.session['cartlist'] = cartlist
        return redirect('/shoppingCart/cart/')
    elif ctype == 'empty':  #清空購物車
        cartlist = []  #設購物車為空串列
        request.session['cartlist'] = cartlist
        return redirect('/shoppingCart/index/')
    elif ctype == 'remove':  #刪除購物車中商品
        del cartlist[int(productid)]  #從購物車串列中移除商品
        request.session['cartlist'] = cartlist
        return redirect('/shoppingCart/cart/')
    return redirect('/shoppingCart/cart/')

def cartorder(request):
    if not request.user.is_authenticated:		#確認登入狀態
        return redirect("/account/login/")
    global cartlist, message, customname, customphone, customaddress, customemail
    global shippingFee
    cartlist1 = cartlist
    total = 0
    for unit in cartlist:  #計算商品總金額
        total += int(unit[3])
    grandtotal = total + shippingFee
    customname1 = customname  #以區域變數傳給模版
    customphone1 = customphone
    customaddress1 = customaddress
    customemail1 = customemail
    message1 = message
    return render(request, "shoppingCart/cartorder.html", locals())

def cartok(request):
    global cartlist, message, customname, customphone, customaddress, customemail
    global shippingFee
    total = 0
    for unit in cartlist:
        total += int(unit[3])
    grandtotal = total + shippingFee
    message = ''
    customname = request.POST.get('CustomerName', '')
    customphone = request.POST.get('CustomerPhone', '')
    customaddress = request.POST.get('CustomerAddress', '')
    customemail = request.POST.get('CustomerEmail', '')
    paytype = request.POST.get('paytype', '')
    customname1 = customname
    if customname=='' or customphone=='' or customaddress=='' or customemail=='':
        message = '姓名、電話、住址及電子郵件皆需輸入'
        return redirect('/cartorder/')
    else:
        unitorder = models.OrdersModel.objects.create(subtotal=total, shipping=shippingFee, grandtotal=grandtotal, customname=customname, customphone=customphone, customaddress=customaddress, customemail=customemail, paytype=paytype) #建立訂單
        for unit in cartlist:  #將購買商品寫入資料庫
            total = int(unit[1]) * int(unit[2])
            unitdetail = models.DetailModel.objects.create(dorder=unitorder, pname=unit[0], unitprice=unit[1], quantity=unit[2], dtotal=total)
        orderid = unitorder.id  #取得訂單id
        mailfrom="你的gmail帳號"  #帳號
        mailpw="你的gmail密碼"  #密碼
        mailto=customemail  #收件者
        mailsubject="織夢數位購物網-訂單通知";  #郵件標題
        mailcontent = "感謝您的光臨，您已經成功的完成訂購程序。\n我們將儘快把您選購的商品郵寄給您！ 再次感謝您支持\n您的訂單編號為：" + str(orderid) + "，您可以使用這個編號回到網站中查詢訂單的詳細內容。\n織夢數位購物網" #郵件內容
        send_simple_message(mailfrom, mailpw, mailto, mailsubject, mailcontent)  #寄信
        cartlist = []
        request.session['cartlist'] = cartlist
        return render(request, "shoppingCart/cartok.html", locals())

def cartordercheck(request):  #查詢訂單
    orderid = request.GET.get('orderid', '')  #取得輸入id
    customemail = request.GET.get('customemail', '')  #取得輸email
    if orderid == '' and customemail == '':  #按查詢訂單鈕
        firstsearch = 1
    else:
        order = models.OrdersModel.objects.filter(id=orderid).first()
        if order == None or order.customemail != customemail:  #查不到資料
            notfound = 1
        else:  #找到符合的資料
            details = models.DetailModel.objects.filter(dorder=order)
    return render(request, "shoppingCart/cartordercheck.html", locals())

def send_simple_message(mailfrom, mailpw, mailto, mailsubject, mailcontent):
    global message
    strSmtp = "smtp.gmail.com:587"  #主機
    strAccount = mailfrom  #帳號
    strPassword = mailpw  #密碼
    msg = MIMEText(mailcontent)
    msg["Subject"] = mailsubject  #郵件標題
    mailto1 = mailto  #收件者
    server = SMTP(strSmtp)  #建立SMTP連線
    server.ehlo()  #跟主機溝通
    server.starttls()  #TTLS安全認證
    try:
        server.login(strAccount, strPassword)  #登入
        server.sendmail(strAccount, mailto1, msg.as_string())  #寄信
    except SMTPAuthenticationError:
        message = "無法登入！"
    except:
        message = "郵件發送產生錯誤！"
    server.quit() #關閉連線