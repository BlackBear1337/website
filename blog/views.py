from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import PostForm
from blog.models import Post, Comment


def index(request):
    post = Post.objects.all()
    return render(request, 'blog/index.html', {'post': post})


def adminpanel(request):
    post = Post.objects.all()
    return render(request, 'blog/adminpanel.html', {'post': post})


def create(request):
    if request.method == 'GET':
        form = PostForm()
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("demo:index")
    context = {
        'form': form
    }
    return render(request, 'blog/create.html', context)


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
    elif request.method == 'POST':
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('demo:edit', pk)
    context = {'form': form, 'title': 'Edit Post'}
    return render(request, 'blog/edit.html', context)


def details(request, pk):
    queryset = get_object_or_404(Post, pk=pk)
    context = {'post': queryset}
    return render(request, 'blog/details.html', context)


def delete(request, pk):
    post_form = Post.objects.get(pk=pk)
    post_form.delete()
    return redirect('demo:index')


def comment(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comment.html', {'comments': comments})
