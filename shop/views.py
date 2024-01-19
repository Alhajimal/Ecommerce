from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *


def home(request):
    return render(request,"shop/index.html")
 
def categories(request):
    category=Category.objects.filter(status=0)
    return render(request,"shop/categories.html",{'category':category})

def categoriesview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context={'products':products,'category':category}
        return render(request,"shop/products/index.html",context)
    else:
        messages.warning(request,"No such category found")
        return redirect('categories')

def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products = Product.objects.filter(slug=prod_slug,status=0).first
            context = {'products':products}


        else:
            messages.error(request,"No such product found")
            return redirect('categories')

    else:
        messages.error(request,"No such category found")
        return redirect('categories')
    return render(request,"shop/products/view.html",context)



