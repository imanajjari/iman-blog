from django import template
from blog.models import Post, Category

register = template.Library()
@register.inclusion_tag('blog/include/blog-popular-posts.html')
def latestposts(arg=4):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/include/blog-post-categories.html')
def postCategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}

# @register.inclusion_tag('blog/include/blog-all-tags.html')
# def allTags():
#     posts = Post.objects.filter(status=1)
#     return {'posts': posts}
