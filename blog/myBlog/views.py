from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404
# from django.http import HttpResponse

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myBlog/post/list.html',{'posts': posts})  


def post_detail(request,id):
    # method 1
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    # return render(request, 'myBlog/post/detail.html',{'post': post})

    # method 2
    post = get_object_or_404(Post, id = id , status = Post.Status.PUBLISHED)
    return render(request, 'myBlog/post/detail.html',{'posts': post})


# def home(request):
#     return render(request, 'home.html')
