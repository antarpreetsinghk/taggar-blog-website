from django.db import models
from PIL import Image
from embed_video.fields import EmbedVideoField


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='media/about_image', blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title


class ImageCategory(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Image category'
        verbose_name_plural = 'Image Categories'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, default='Image')
    image = models.ImageField(upload_to='media/gallery_images')
    description = models.TextField(default='Taggar Associates gallery Image')

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            new_img = (1280, 720)
            img.thumbnail(new_img)
            img.save(self.image.path, format="JPEG", quality=70)

    class Meta:
        ordering = ('-pk', )
        verbose_name = 'Image'
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return f'{self.title} - {self.pk}'


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
