from django.db import models


# Create your models here.
class HeroBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Tiêu đề banner", blank=True)
    subtitle = models.TextField(verbose_name="Mô tả ngắn", blank=True)
    image = models.ImageField(upload_to="banners/", verbose_name="Ảnh Banner Full Page")
    order = models.PositiveIntegerField(default=0, verbose_name="Thứ tự hiển thị")
    is_active = models.BooleanField(default=True, verbose_name="Kích hoạt")

    class Meta:
        ordering = ["order"]
        verbose_name = "Banner Trang Chủ"
        verbose_name_plural = "2. Banner Trượt Đầu Trang"


class CompanyMetric(models.Model):
    label = models.CharField(
        max_length=255, verbose_name="Nhãn (VD: Tổng diện tích sàn XD)"
    )
    value = models.CharField(max_length=100, verbose_name="Con số (VD: 500.000)")
    unit = models.CharField(
        max_length=50, verbose_name="Đơn vị (VD: m2 sàn XD)", blank=True
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Thứ tự")

    class Meta:
        ordering = ["order"]
        verbose_name = "Con số ấn tượng / Chỉ số"
        verbose_name_plural = "1. Con số năng lực"


class PmisIntro(models.Model):
    title = models.CharField(max_length=255, default="Hệ thống PMIS")
    description = models.TextField(verbose_name="Mô tả hệ thống PMIS")
    image = models.ImageField(upload_to="pmis/", verbose_name="Ảnh mình họa PMIS")

    class Meta:
        verbose_name = "Tính năng PMIS"
        verbose_name_plural = "3. Tính năng Hệ thống PMIS"
