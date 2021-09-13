from .models import AboutUs, ImageCategory, Gallery, Video, ContactUs, Faqs, PrivacyPolicy, TermsOfUse, VideoCategory
from blog.models import Category
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class AboutView(ListView):
    template_name = "page/about.html"
    model = AboutUs

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['categories_name'] = Category.objects.order_by('-id')
        return context


class ContactView(ListView):
    template_name = "page/contact.html"
    model = ContactUs


class FaqView(ListView):
    template_name = "page/faq.html"
    model = Faqs


class PrivacypollicyView(ListView):
    template_name = "page/privacy.html"
    model = PrivacyPolicy


class TermsofuseView(ListView):
    template_name = "page/terms.html"
    model = TermsOfUse


def images_list(request, category_slug=None):
    category = None
    categories = ImageCategory.objects.all()
    images = Gallery.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(images, 12)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    if category_slug:
        category = get_object_or_404(ImageCategory, slug=category_slug)
        images = Gallery.objects.filter(category=category).order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(images, 12)
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'categories': categories,
        'images': images
    }
    return render(request, 'page/gallery.html', context)


def videos_list(request, category_slug=None):
    category = None
    categories = VideoCategory.objects.all()
    videos = Video.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(videos, 10)
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    if category_slug:
        category = get_object_or_404(VideoCategory, slug=category_slug)
        videos = Video.objects.filter(category=category).order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(videos, 10)
        try:
            videos = paginator.page(page)
        except PageNotAnInteger:
            videos = paginator.page(1)
        except EmptyPage:
            videos = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'categories': categories,
        'videos': videos
    }
    return render(request, 'page/videos.html', context)
