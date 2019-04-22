from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post,Category,Tag
from comments.forms import CommentForm
import markdown
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={
        'title':'首页',
        'welcome':'这是第一个页面',
        'post_list':post_list,
    })

def detail(request, pk):
    post = get_object_or_404(Post,pk=pk)

    # 增加评论数
    post.increase_views()
    post.body = markdown.markdown(
        post.body,
        extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    # 导入from表单
    form = CommentForm()
    # 获取所有评论并且显示
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form':form,
        'comment_list':comment_list,
    }

    return render(request,'blog/detail.html',context=context)

def archive(request, year, month):
    post_list = Post.objects.filter(
        created_time__year = year,
        created_time__month = month,
    ).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request, pk):
    category = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=category).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})