from django.contrib import admin
from .models import AboutUs, ContactUs, Faqs, PrivacyPolicy, TermsOfUse


admin.site.register(AboutUs)
admin.site.register(ContactUs)
admin.site.register(Faqs)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfUse)
