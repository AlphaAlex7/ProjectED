from django.db import models
from django.db.models import *
from django.contrib.auth.models import User
from django.shortcuts import reverse


class PostCategory(models.Model):
    title = CharField(verbose_name="Категория", max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class PostModel(models.Model):
    title = CharField(verbose_name="Заголовок", max_length=200)
    text = TextField(verbose_name="Текст")
    date_pub = DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    author = ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="author")
    category = ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True, verbose_name="Категория",
                          related_name="category_post")
    img_preview = ImageField(upload_to='posts/preview/%Y/%m/%d', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

    def get_comment_counts(self):
        return PostComment.objects.filter(post=self.pk).count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-date_pub']


class PostComment(models.Model):
    author = ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="author_comment")
    text = TextField(verbose_name="Комментарий")
    date_pub = DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    post = ForeignKey(PostModel, on_delete=models.CASCADE, verbose_name="Пост", related_name="post_id")

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-date_pub']
