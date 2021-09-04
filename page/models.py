from django.db import models
from embed_video.fields import EmbedVideoField


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='media/about_image', blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title


class VideoCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'video category'
        verbose_name_plural = 'Video Categories'

    def __str__(self):
        return self.name


class Video(models.Model):
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    video_path = EmbedVideoField()

    def __str__(self):
        return self.title


class TermsOfUse(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Terms Of Use"

    def __str__(self):
        return self.title


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Privacy Policy"

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.title


class Faqs(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.title
