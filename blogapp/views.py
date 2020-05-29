from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticle
from django.contrib.auth import authenticate, login


def index(request):     #function for index page 
    blogs = BlogArticle.objects.all()       #to get details of all the blogs
    if request.method == "POST":        
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username = uname, password = pwd)       #to authenticate user using entered username and password

        if user is not None:
            login(request, user)        #login the user
            return render(request, "main.html", { "blogs" : blogs, "user" : user})      #this will display the main html file with blogs of a user

    return render(request, "main.html", { "blogs" : blogs, "user" : None})

def createBlog(request):        #function to enter details about a blog
    blogs = BlogArticle.objects.all()
    newBlog = BlogArticle()
    newBlog.title = request.POST['title']
    newBlog.blog_content = request.POST['blog_content']
    newBlog.author = request.user
    newBlog.save()
    return render(request, "main.html", { "blogs" : blogs, "user" : request.user})
