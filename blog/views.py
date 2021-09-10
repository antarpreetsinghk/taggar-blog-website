from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm, UserRegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    context = {
        'main':Post.objects.filter(main=True, published=True).order_by('-id')[:4],
        'recent_posts': Post.objects.filter(published=True).order_by('-id')[:10],
        'categories': Category.objects.all().order_by('-id')[:10]
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
    posts = Post.objects.filter(post_category=category, published=True).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 12)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'posts': posts,
        'categories_name': Category.objects.all().order_by('-id'),
    }
    return render(request, 'blog/categories.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'blog/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


@login_required
def profile(request):
    return render(request, 'blog/profile.html')


def auther(request, id):
    auther = get_object_or_404(User, id=id)
    posts = Post.objects.filter(author=auther, published=True).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 12)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'auther': auther,
        'posts': posts,
        'categories_name': Category.objects.all().order_by('-id'),
    }
    return render(request, 'blog/auther.html', context)


def search(request):
    query = request.GET['q']
    context = {
        'posts': Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query), published=True),
        'categories_name': Category.objects.all().order_by('-id'),
    }
    return render(request, 'blog/search.html', context)
