from django.db import models


# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Tên loại dự án (VD: Nhà ở dân dụng, Khách sạn...)"
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Loại Dự án"
        verbose_name_plural = "Các Loại Dự án"

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(
        ProjectCategory, on_delete=models.CASCADE, related_name="projects"
    )
    title = models.CharField(max_length=255, verbose_name="Tên dự án")
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(
        upload_to="projects/thumbnails/", verbose_name="Ảnh đại diện (Slide 10)"
    )
    address = models.CharField(max_length=255, verbose_name="Địa chỉ")
    investor = models.CharField(max_length=255, verbose_name="Chủ đầu tư")

    # Chi tiết (Slide 11)
    overview = models.TextField(verbose_name="Đoạn giới thiệu chung / Thông số dự án")
    is_featured = models.BooleanField(
        default=False, verbose_name="Nổi bật (Hiển thị trang chủ)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Dự án"
        verbose_name_plural = "Danh sách Dự án"


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="gallery"
    )
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(
        max_length=255, blank=True, verbose_name="Mô tả dưới ảnh"
    )
