from django.shortcuts import render, redirect
from . import models
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.text import MIMEText

def index(request):

    return render(request, "index.html")

def detail(request, productid=None):

    return render(request, "detail.html")

def cart(request):

    return render(request, "cart.html", locals())

def addtocart(request, ctype=None, productid=None):

    return redirect('/cart/')

'''
def cartorder(request):
    
    return render(request, "cartorder.html", locals())
'''
def cartok(request):

    return render(request, "cartok.html", locals())

def cartordercheck(request):  #查詢訂單

    return render(request, "cartordercheck.html", locals())

def send_simple_message(mailfrom, mailpw, mailto, mailsubject, mailcontent):
    global message