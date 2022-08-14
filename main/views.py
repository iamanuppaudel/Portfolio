from django.shortcuts import render
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

BLOGS_PER_PAGE = 4

# Create your views here.
def index(request):
    projects = Portfolio.objects.all()
    context={
        'projects':projects,
    }
    return render(request, "main/index.html",context)

def about(request):
    context={}
    return render(request, "main/about.html",context)

def portfolio(request):
    projects = Portfolio.objects.all()

    context={
        'projects':projects,
    }
    return render(request, "main/portfolio.html",context)

def blog(request):
    blogs = Blog.objects.all().order_by('-date_added')
    page = request.GET.get('page',1)
    blog_paginator = Paginator(blogs, BLOGS_PER_PAGE)

    try:
        blogs = blog_paginator.page(page)
    except EmptyPage:
        blogs = blog_paginator.page(blog_paginator.num_pages)
    except:
        blogs = blog_paginator.page(BLOGS_PER_PAGE)

    number = blogs.number
    loop = blog_paginator.get_elided_page_range(number,on_each_side=2, on_ends=1)

    popularpost = Blog.objects.all().order_by('-view_count')[:6]

    context={
        "blogs":blogs,
        "page_obj":blogs,
        "is_paginated":True,
        "paginator":blog_paginator,
        "loop":loop,
        "popularpost":popularpost,

    }
    return render(request, "main/blog.html",context)

def blogdetail(request,pk):

    # <<<  for  updating view count
    blog_object= Blog.objects.get(id=pk)
    blog_object.view_count =blog_object.view_count + 1
    blog_object.save()
    # view count updated >>>
    blog = Blog.objects.get(id=pk)
    popularpost = Blog.objects.all().order_by('-view_count')[:6]

    context={
        'blogdetail':blog,
        "popularpost":popularpost,

    }
    return render(request,"main/blog-single.html",context)

def detailportfolio(request,pk):
    project = Portfolio.objects.get(id=pk)
    context={
        "project": project
    }
    return render(request,"main/portfolio-single3.html", context)

def contact(request):
    context={}
    return render(request, "main/contact.html",context)
