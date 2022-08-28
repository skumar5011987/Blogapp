from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import RegistrationForm, SigninForm, UserPost
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.models import Group


# home.
def home(request):
    posts = Post.objects.all()
    return render(request, 'foodblogapp/home.html', {'posts': posts})


# About.
def about(request):
    return render(request, 'foodblogapp/about.html')


# Contact.
def contact(request):
    return render(request, 'foodblogapp/contact.html')


# Dashbord.
def dashboard(request):
    if request.user.is_authenticated:
        # posts = Post.objects.filter(uname=request.user)
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'foodblogapp/dashboard.html',
                      {'posts': posts, 'full_name': full_name, 'groups': gps})
    else:
        return HttpResponseRedirect('/')


# Sign-up.
def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(
                    request, 'Congratulations!!! Now you are one of us.')
                user = form.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
        else:
            form = RegistrationForm()
        return render(request, 'foodblogapp/signup.html', {'form': form})


# Sign-in .
def signin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SigninForm(request=request, data=request.POST)

            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Sign-in successsfully!!!')
                    return redirect('dashboard')
        else:
            form = SigninForm()
            return render(request, 'foodblogapp/signin.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

    return render(request, 'foodblogapp/signin.html', {'form': form})


# Add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if not User.objects.filter(username=request.POST['uname']):
                messages.error(request, 'Username does not exist.')
                return redirect('add_post')

            form = UserPost(request.POST)
            if form.is_valid():
                messages.success(request, 'Post added successfully!!!')
                form.save()
                return HttpResponseRedirect('/add_post/')
        else:
            form = UserPost()
            return render(request, 'foodblogapp/add_post.html', {'form': form})
    else:
        return HttpResponseRedirect('/home/')


# Update post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            data = Post.objects.get(pk=id)
            record = UserPost(request.POST, instance=data)
            if record.is_valid():
                record.save()
                messages.success(request, 'Post updated successfully!!!')
        else:
            data = Post.objects.get(pk=id)
            record = UserPost(instance=data)
        return render(request, 'foodblogapp/update_post.html', {'form': record})
    else:
        return HttpResponseRedirect('/login/')


# Delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            record = Post.objects.get(pk=id)
            record.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


# Logout.
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
