from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='media/about_image', blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Us"

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
