from .models import AboutUs,Video, ContactUs, Faqs, PrivacyPolicy, TermsOfUse, VideoCategory
from blog.models import Category
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404


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


def gallery(requst):
    return render(requst, 'page/gallery.html')


def videos_list(request, category_slug=None):
    category = None
    categories = VideoCategory.objects.all()
    videos = Video.objects.all()
    if category_slug:
        category = get_object_or_404(VideoCategory, slug=category_slug)
        videos = Video.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'videos': videos
    }
    return render(request, 'page/videos.html', context)
