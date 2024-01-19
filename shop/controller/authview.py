from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from shop.forms import CustomUserForm
from shop.models import Contact

def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully!Login to Continue")
            return redirect('/login')
    context={'form':form}
    return render(request,"shop/auth/register.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect("/")
    else:
        if request.method=="POST":
            name = request.POST.get('username')
            passwordd = request.POST.get('password') 

            user = authenticate(request,username=name,password=passwordd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Succcessfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password")
                return redirect('/login')
        return render(request,"shop/auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/")


def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        description=request.POST.get("description")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,description=description,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"We will get back to you soon...")
        return render(request,"shop/auth/contact.html")
    return render(request,"shop/auth/contact.html")
      
       