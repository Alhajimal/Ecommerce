from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop.models import Product,Wishlist

@login_required(login_url='loginpage')

def index(request):
    wishlist = Wishlist.objects.filter(user=request.user.id)
    context = {'wishlist':wishlist}
    return render(request,'shop/wishlist.html',context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':"Product already in wishlist"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':"Product added to wishlist"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to continue"})
            
    return redirect('/')

def deletewishlistitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if request.user.is_authenticated:
            if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"Product removed from wishlist"})
            else:
                Wishlist.objects.create(user=request.user,product_id=prod_id)
                return JsonResponse({'status':"Product not found in wishlist"})


        else:
            return JsonResponse({'status':"Login to continue"})
        

    return redirect('/')
