from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'post_form.html')

def post_create(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        post = Post(
            author=author,
            content=content
        )
        post.save()
        return render(request, 'post_created.html', {'author': author, 'content': content})
    return render(request, 'post_form.html')

def post_list(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'post_list.html', {'posts': posts})
