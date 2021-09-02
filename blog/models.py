from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    class Meta:
         verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/posts_images')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    main = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            new_img = (1280, 720)
            img.thumbnail(new_img)
            img.save(self.image.path, format="JPEG", quality=70)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-details', kwargs={'id': self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    reply = models.ForeignKey('Comment', null=True, blank=True, related_name="replies", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.author.username))
