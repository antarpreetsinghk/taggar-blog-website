from .models import AboutUs, ContactUs, Faqs, PrivacyPolicy, TermsOfUse
from blog.models import Category
from django.views.generic import ListView
from django.shortcuts import render


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


def videos(requst):
    return render(requst, 'page/videos.html')
