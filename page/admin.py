from django.contrib import admin
from .models import AboutUs,Gallery, Video, VideoCategory, ContactUs, Faqs, PrivacyPolicy, TermsOfUse


admin.site.register(AboutUs)
admin.site.register(Gallery)

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(VideoCategory, VideoAdmin)

admin.site.register(Video)
admin.site.register(ContactUs)
admin.site.register(Faqs)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfUse)
