from django.db import models
import os
from django.utils.text import slugify


def drawing_upload_path(instance, filename):
    name, ext = os.path.splitext(filename)
    clean_name = slugify(name)
    return f"drawings/{clean_name}{ext}"


class BimServiceCategory(models.Model):
    LAYOUT_CHOICES = (
        ("standard_3d", "BIM 3D Layout (Gallery Model & Công đoạn)"),
        ("drawing_flip", "Triển khai bản vẽ (Flipbook & Tool xung đột)"),
        ("placeholder_4d", "BIM 4D Layout (Sắp ra mắt / Video)"),
        ("quantity_5d", "BIM 5D Layout (Khối lượng & Tool Revit)"),
        ("operation_6d", "BIM 6D Layout (IFC / Panorama 360)"),
        ("custom_dynamic", "Layout Linh hoạt (Dành cho Dịch vụ mới phát sinh)"),
    )

    name = models.CharField(
        max_length=255, verbose_name="Tên dịch vụ (VD: BIM 3D, BIM 5D...)"
    )
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True, verbose_name="Mô tả ngắn")
    order = models.PositiveIntegerField(default=0, verbose_name="Thứ tự hiển thị")
    layout_type = models.CharField(
        max_length=50,
        choices=LAYOUT_CHOICES,
        default="custom_dynamic",
        verbose_name="Kiểu Giao diện Rendering",
    )
    is_active = models.BooleanField(default=True, verbose_name="Kích hoạt")
    is_coming_soon = models.BooleanField(
        default=False, verbose_name="Chưa triển khai (Coming Soon)"
    )

    class Meta:
        verbose_name = "Dịch vụ BIM"
        verbose_name_plural = "QUẢN LÝ DỊCH VỤ BIM"
        ordering = ["order"]

    def __str__(self):
        return self.name


# 1. Chi tiết cho BIM 3D (Slide 4)
class Bim3DDetail(models.Model):
    category = models.OneToOneField(
        BimServiceCategory, on_delete=models.CASCADE, related_name="detail_3d"
    )
    content_tkcs = models.TextField(verbose_name="Nội dung BIM TKCS", blank=True)
    content_tkbvtc = models.TextField(verbose_name="Nội dung BIM TKBVTC", blank=True)
    content_bvhc = models.TextField(verbose_name="Nội dung BIM BVHC", blank=True)

    class Meta:
        verbose_name = "Chi tiết BIM 3D"
        verbose_name_plural = "Quản lý Ảnh & Nội dung BIM 3D"


class Bim3DImage(models.Model):
    detail_3d = models.ForeignKey(
        Bim3DDetail, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="bim_3d/")
    caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Chú thích (VD: Mô hình Cơ điện, Kết cấu...)",
    )


# 2. Chi tiết cho Triển khai bản vẽ (Slide 5)
class DrawingDetail(models.Model):
    category = models.OneToOneField(
        BimServiceCategory, on_delete=models.CASCADE, related_name="detail_drawing"
    )
    embed_conflict_tool_url = models.URLField(
        blank=True, verbose_name="Link nhúng Tool Quản lý xung đột/So sánh bản vẽ"
    )

    class Meta:
        verbose_name = "Chi tiết Triển khai bản vẽ"
        verbose_name_plural = "Quản lý Bản vẽ & Tool Xung đột"


class DrawingFile(models.Model):
    drawing_detail = models.ForeignKey(
        DrawingDetail, on_delete=models.CASCADE, related_name="drawings"
    )
    file_or_image = models.FileField(
        upload_to=drawing_upload_path, verbose_name="File ảnh/PDF bản vẽ"
    )
    title = models.CharField(max_length=255, blank=True, verbose_name="Tiêu đề bản vẽ")


# 3. Chi tiết cho BIM 5D & 6D (Slide 7, 9)
class Bim5DDetail(models.Model):
    category = models.OneToOneField(
        BimServiceCategory, on_delete=models.CASCADE, related_name="detail_5d"
    )
    description = models.TextField(verbose_name="Mô tả khối lượng")
    video_url = models.URLField(blank=True, verbose_name="Link Clip giới thiệu")
    materials_db_info = models.TextField(
        verbose_name="Thông tin CSDL Vật tư/Công việc", blank=True
    )
    revit_tool_info = models.TextField(
        verbose_name="Thông tin Tool BIM 5D Connect Revit", blank=True
    )

    class Meta:
        verbose_name = "Chi tiết BIM 5D"
        verbose_name_plural = "Quản lý BIM 5D (Khối lượng & Revit)"


class Bim6DDetail(models.Model):
    category = models.OneToOneField(
        BimServiceCategory, on_delete=models.CASCADE, related_name="detail_6d"
    )
    description = models.TextField(verbose_name="Mô tả vận hành")
    video_url = models.URLField(blank=True, verbose_name="Link Clip giới thiệu")
    ifc_file = models.FileField(
        upload_to="ifc/", blank=True, verbose_name="File IFC Upload"
    )

    class Meta:
        verbose_name = "Chi tiết BIM 6D"
        verbose_name_plural = "Quản lý BIM 6D (Vận hành & Ảnh 360)"


class Bim6DPanoramaImage(models.Model):
    detail_6d = models.ForeignKey(
        Bim6DDetail, on_delete=models.CASCADE, related_name="panorama_images"
    )
    image_url = models.CharField(
        max_length=500, verbose_name="Link ảnh Panorama 360 hoặc đường dẫn file"
    )
    caption = models.CharField(
        max_length=255, blank=True, verbose_name="Tên khu vực / Chú thích"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
