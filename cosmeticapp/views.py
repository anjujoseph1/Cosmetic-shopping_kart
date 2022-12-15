from django.shortcuts import render,reverse,redirect,get_object_or_404
from.models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request,c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(Categ, slug=c_slug) 
        prodt = Products.objects.filter(category=c_page, available=True) 
    else:
        prodt = Products.objects.all().filter(available=True) 
    cat = Categ.objects.all()

    prod=Products.objects.all()
    return render(request,'home.html',{'pr':prod,'ct':cat})

def productdetails(request,c_slug,product_slug):
    try:
        proddet=Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'view.html',{'pr':proddet})

# cart section begins:

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id


def cartdetails(request,tot=0,count=0,c=0,c_item=None):
    try:
        ct=CartList.objects.get(cart_id=c_id(request))
        c_item=CartItem.objects.filter(cart=ct,active=True)
        for i in c_item:
            tot += (i.prod.price * i.quan)
            c = c + 1
        count = tot + 100
    except ObjectDoesNotExist:
        pass
    context={
        'ci':c_item,
        't':tot,
        'cn':count,
        'c':c
    }
    return render(request,'cart.html',context)
    
def add_cart(request,product_id):
    pro=Products.objects.get(id=product_id)
    try:
        ct=CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        ct=CartList.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        ct_item=CartItem.objects.get(prod=pro,cart=ct)
        if ct_item.quan < ct_item.prod.stock:
            ct_item.quan += 1
        ct_item.save()
    except CartItem.DoesNotExist:
        ct_item=CartItem.objects.create(prod=pro,quan=1,cart=ct)
        ct_item.save()
    return redirect('cart_details')

def min_cart(request,product_id):
    ct=CartList.objects.get(cart_id=c_id(request))
    pro=get_object_or_404(Products,id=product_id)
    c_item=CartItem.objects.get(prod=pro,cart=ct)
    if c_item.quan > 1:
        c_item.quan -= 1
        c_item.save()
    else:
        c_item.delete()
    return redirect('cart_details')

def remove(request,product_id):
    ct=CartList.objects.get(cart_id=c_id(request))
    pro=get_object_or_404(Products,id=product_id)
    c_item=CartItem.objects.get(prod=pro,cart=ct)
    c_item.delete()
    return redirect('cart_details')

def loginform(request):
    return render(request,'login.html')

def registerform(request):
    return render(request,'register.html')