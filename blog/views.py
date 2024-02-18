from django.shortcuts import render,get_object_or_404
from .models import Blog,Comment
# Create your views here.

def blog_list(request):
    tag = request.GET.get('tag')
    if tag:
        blog = Blog.objects.filter(is_published=True,tags__name=tag).order_by('-created')
        return render(request, 'blog/blog_list.html', {'blog': blog})
    blog = Blog.objects.filter(is_published=True).order_by('-created')
    return render(request,'blog/blog_list.html',{'blog':blog})

def blog_details(request,slug):
    blog = get_object_or_404(Blog,slug=slug)
    recent_blog = Blog.objects.filter(is_published=True).order_by('-created')[0]
    comments = blog.comments.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        comment = Comment.objects.create(blog=blog,name=name,email=email,body=body)
    return render(request,'blog/blog_details.html',{'blog':blog,'recent_blog':recent_blog,'comments':comments})