from django.contrib import admin
from .models import AboutUs, ImageCategory, Gallery, Video, VideoCategory, ContactUs, Faqs, PrivacyPolicy, TermsOfUse


admin.site.register(AboutUs)

class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ImageCategory, ImageAdmin)

admin.site.register(Gallery)

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(VideoCategory, VideoAdmin)

admin.site.register(Video)
admin.site.register(ContactUs)
admin.site.register(Faqs)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfUse)
