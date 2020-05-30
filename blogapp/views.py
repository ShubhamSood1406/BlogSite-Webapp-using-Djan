from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogArticle
from django.contrib.auth import authenticate, login

#function for index page
def index(request): 
    #to get details of all the blogs
    blogs = BlogArticle.objects.all()
    if request.method == "POST":        
        uname = request.POST['username']
        pwd = request.POST['password']
        #to authenticate user using entered username and password
        user = authenticate(username = uname, password = pwd)

        # if user is Not None i.e we have user detail
        if user is not None:
            #login the user
            login(request, user)
            
            #this will display the main html file with blogs of a user
            return render(request, "main.html", { "blogs" : blogs, "user" : user})

    return render(request, "main.html", { "blogs" : blogs, "user" : None})

def createBlog(request):        #function to enter details about a blog
    blogs = BlogArticle.objects.all()
    newBlog = BlogArticle()
    newBlog.title = request.POST['title']
    newBlog.blog_content = request.POST['blog_content']
    newBlog.author = request.user
    newBlog.save()
    return render(request, "main.html", { "blogs" : blogs, "user" : request.user})
