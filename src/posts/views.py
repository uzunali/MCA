from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from .models import Post
from marketting.models  import Signup
from django.db.models import Count,Q


def search(request):
    queryset=Post.objects.all()
    query = request.GET.get('q')
    if queryset:
        queryset=queryset.filter(
            Q(title__icontains=query)|
            Q(overview__icontains=query)
        ).distinct()
    
    context={
        'queryset':queryset
    }
    return render (request, 'search_results.html',context)


def get_category_count():
    queryset=Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset


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
    category_count=get_category_count()
    most_recent=Post.objects.order_by('-timestamp')[:3]
    post_list=Post.objects.all()
    paginator = Paginator(post_list,4)
    page_request_var = 'page'
    page=request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)

    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

        
    context={
        'queryset':paginated_queryset,
        'most_recent':most_recent,
        'page_request_var':page,
        'category_count':category_count

    }
    return render(request, 'blog.html', context)

def post(request):
    return render(request, 'post.html', {})