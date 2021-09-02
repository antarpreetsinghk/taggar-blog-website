from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from .forms import UserRegisterForm, CommentForm
from django.http import HttpResponseRedirect


def home(request):
    context = {
        'main':Post.objects.filter(main=True, published=True).order_by('-id')[:4],
        'recent_posts': Post.objects.filter(published=True).order_by('-id')[:7],
        'categories': Category.objects.all().order_by('-id')
    }
    return render(request, 'blog/home.html', context)


def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, author=request.user, content=content, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'categories': Category.objects.all().order_by('-id')
    }
    return render(request, 'blog/post_details.html', context)


def categories(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug) 
    context = {
        'category': category,
        'posts': Post.objects.filter(post_category=category, published=True),
        'categories_name': Category.objects.all().order_by('-id'),
    }
    return render(request, 'blog/categories.html', context)
