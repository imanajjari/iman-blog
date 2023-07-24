from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

# Create your views here.

def blog_view (request, **kwargs):
    posts = Post.objects.filter(status=1).order_by('-published_date')
    # if kwargs['author_username']:
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    try:
        posts = Paginator(posts, 2)
        page_number = request.GET.get('page')
    except PageNotAnInteger or EmptyPage:
        posts = posts.get_page(1)
    # except EmptyPage:
    #     posts = posts.get_page(1)
    posts= posts.get_page(page_number)
    content = {'posts':posts}
    return render(request, 'blog/blog-home.html',content)

def blog_single (request, post_id):
    post = Post.objects.get(pk=post_id, status=1)
    if not post.login_require :
        content = {'post':post}
        return render(request, 'blog/blog-single.html', content)
    else:
        return redirect('accounts:login')

def blog_detail (request):
    posts = Post.objects.filter(status=1)
    content = {'posts':posts}
    return render(request, 'blog/blog-home.html',content)

def blog_category(request, cat_name):
    # category = Category.objects.get(name=cat_name)
    posts= Post.objects.filter(status=1, category__name=cat_name)
    content = {'posts':posts}
    return render(request,'blog/blog-home.html', content)

def blog_search(request):
    posts= Post.objects.filter(status=1)
    if request.method=='GET':
        if s:=request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    content = {'posts':posts}
    return render(request,'blog/blog-home.html', content)


