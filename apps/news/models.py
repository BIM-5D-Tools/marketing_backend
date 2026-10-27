from django.db import models


# Create your models here.
class NewsArticle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Tiêu đề tin tức")
    slug = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to="news/", verbose_name="Ảnh bìa")
    summary = models.TextField(verbose_name="Mô tả ngắn")
    content = models.TextField(verbose_name="Nội dung bài viết")
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tin tức"
        verbose_name_plural = "Danh sách Tin tức"
