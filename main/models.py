from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone
from django.urls import reverse


class Main(models.Model):
    logo = models.ImageField(upload_to='logo')

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

class Hero(models.Model):
    image = models.ImageField(upload_to='ImgHero')
    genre = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    views = models.IntegerField()
    transcription = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("anime-details", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Главный тайтл'
        verbose_name_plural = 'Главные тайтлы'

class Blog(models.Model):
    photo = models.ImageField(upload_to='ImgBlog')
    title = models.CharField(max_length=255)
    published_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("blog-details", kwargs={"id": self.id})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# class Comment(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
#     text = models.TextField("Текст коментария")
#     created_at = models.DateTimeField(auto_now_add=True)
#     parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
#
#     def __str__(self):
#         return f"Comment by{self.user.username} on {self.blog.title}"
#
#     def is_reply(self):
#         return self.parent is not None

