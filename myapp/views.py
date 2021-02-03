from django.shortcuts import render
from myapp.models import Post
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.http import HttpResponse

per_page = 2
def index(request):
    has_next = 1
    count = Post.objects.count()
    if count <=per_page:
        has_next = 0
    posts = Post.objects.all()[0:per_page]
    return render(request, 'index.html', {'posts': posts,"has_next":has_next})
    

def lazy_load_posts(request):
    page = request.POST.get('page')
    allPosts = Post.objects.all()
    paginator = Paginator(allPosts, per_page)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
   
    posts_html = loader.render_to_string(
        'posts.html',
        {'posts': posts}
    )

    output_data = {
        'posts_html': posts_html,
        'has_next': 1 if posts.has_next() == True else 0,   
        'page_number' : int(page)+1
    }

    return JsonResponse(output_data)

# listing of single post
def view_post(request,getId):
    post = Post.objects.get(id = getId)
    return render(request, 'view.html', {'post': post})


# save bulk data in database
def save_posts(request):
    count = Post.objects.count()
    html = "Add data in databse process started \n"
    res = []
    
    for i in range(1,501):
        res.append(Post(name="test"+str(i),description="test"+str(i),price=i))
    
    Post.objects.bulk_create(
        res
    )

    html += "Data addedd successfullyy!!!"

    return HttpResponse(html)    