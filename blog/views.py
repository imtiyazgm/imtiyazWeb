from unicodedata import category
from django.shortcuts import redirect, render
from django.template import context
from .models import Category, Blog
# import forms
from . forms import BlogForm, CategoryForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def blogList(request):
    
    category =request.GET.get('category')
    
    if category == None:
        blogList = Blog.objects.all()
    else:
        blogList = Blog.objects.filter(blogCategory__name=category)
     
    categoryList = Category.objects.all()

    context= {'blogList':blogList, 'categoryList':categoryList}
    return render(request, 'blog/blogList.html', context)

# Table View
def blogTableList(request):
    
    category =request.GET.get('category')
    
    if category == None:
        blogTableList = Blog.objects.all()
    else:
        blogTableList = Blog.objects.filter(blogCategory__name=category)
     
    categoryList = Category.objects.all()

    context= {'blogList':blogTableList, 'categoryList':categoryList}
    return render(request, 'blog/blogTableList.html', context)    



def blogDetails(request, pk):
    blogobj =Blog.objects.get(id=pk)
    context={'blogobj':blogobj}
    
    return render(request,"blog/blogDetails.html", context )
    
@login_required(login_url = 'loginPage')


def creatBlog(request):
    page = 'CreatBlog'
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    
    
    context = {'form':form}

    return render(request, "blog/blog_form.html", context)

@login_required(login_url = 'loginPage')    
def updateBlog(request, pk):
    blogobj = Blog.objects.get(id=pk)
    
    form = BlogForm(instance = blogobj)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blogobj)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    
    context = {'form':form}
    return render(request, "blog/blog_form.html", context)


@login_required(login_url = 'loginPage')    
def deleteBlog(request, pk):
    blogobj = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blogobj.delete()
        return redirect('blog_list')
    context = {'blogobj':blogobj}
    return render(request, "blog/deleteBlog.html", context)


# create category 
@login_required(login_url = 'loginPage')
def creatCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    
    
    context = {'form':form}

    return render(request, "blog/blog_form.html", context)
