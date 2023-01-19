from django.shortcuts import render,HttpResponseRedirect 
from .forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.
#home
def home(request):
    post=Post.objects.all
    return render(request,'app/home.html',{'post':post})

#about page
def about(request):
    return render(request,'app/about.html')
#contact page
def contact(request):
    return render(request,'app/contact.html')
#dashboard page
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'app/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')
#logout page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
#Signup page
def user_signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation!! you have become an Author')
            form.save()
            group=Group.objects.get(name='user')
            user.groups.add(group)
    else:
        form=SignupForm()        
    return render(request,'app/signup.html',{'form':form})
#login page
def user_login(request):
  if not request.user.is_authenticated:
    if request.method=='POST':
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Successfully')
                return HttpResponseRedirect('/dashboard/')
    else:
        form=LoginForm()
    return render(request,'app/login.html',{'form':form})
  else:
    return HttpResponseRedirect('/dashboard/')                      


 # Add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                post=Post(title=title,desc=desc)
                post.save()
                group=Group.objects.all()
                form=PostForm()
        else:
            form=PostForm()           
        return render(request,'app/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')       
 # Add update post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)                     
        return render(request,'app/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')       
 # Add new post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')       