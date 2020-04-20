from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import data

# Create your views here.

def signup(request):

    if request.method == 'POST':
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        username= request.POST['username']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']


        if(pass1==pass2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'email taken')
                return redirect('signup')

            else:
                user = User.objects.create_user(password = pass1, username= username, first_name=firstname, last_name=lastname)
                user.save()
                messages.info(request,'user created')
                return redirect('signin')

        else:
            messages.info(request,'password not match')
            return redirect('signup')

    return render(request,'signup.html')




def signin(request):
     if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('congo')

        else:
            messages.info(request,"invalid")
            return redirect('signin')

     else:
        return render(request,'signin.html')


def congo(request):
    return render(request,'congo.html')


