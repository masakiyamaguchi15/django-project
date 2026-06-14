from django.shortcuts import render, redirect
from .models import Post

def index(request):
    return render(request, 'post_form.html')

def post_create(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        request.session['author'] = author
        post = Post(
            author=author,
            content=content
        )
        post.save()
        return redirect('simplechat:post_list')
    return render(request, 'post_form.html')

def post_list(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'post_list.html', {'posts': posts})
