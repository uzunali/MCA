from django.shortcuts import render
from .models import Post
from marketting.models  import Signup


def index(request):
    quesryset = Post.objects.filter(featured=True)
    latest= Post.objects.order_by('-timestamp')[0:3]

    if request.method=='POST':
        email= request.POST['email']
        new_signup=Signup()
        new_signup.email=email
        new_signup.save()
         
    featured={
        'object_list':quesryset,
        'latest':latest
    }
    return render(request, 'index.html', featured)


def blog(request):
    return render(request, 'blog.html', {})

def post(request):
    return render(request, 'post.html', {})