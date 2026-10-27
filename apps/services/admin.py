# backend/apps/services/admin.py
from django.contrib import admin
from .models import (
    BimServiceCategory,
    Bim3DDetail,
    Bim3DImage,
    DrawingDetail,
    DrawingFile,
    Bim5DDetail,
    Bim6DDetail,
    Bim6DPanoramaImage,
)


# --- 1. CÁC INLINE PHỤ CHO TỪNG BỘ PHẬN ---
class Bim3DImageInline(admin.TabularInline):
    model = Bim3DImage
    extra = 1
    verbose_name = "Ảnh Mô Hình 3D"
    verbose_name_plural = (
        "Danh sách Ảnh Mô Hình 3D (Kết cấu / Kiến trúc / Cơ điện MEP)"
    )


class DrawingFileInline(admin.TabularInline):
    model = DrawingFile
    extra = 1
    verbose_name = "Bản vẽ"
    verbose_name_plural = "Danh sách Bản vẽ lật trang (Flipbook)"


class Bim6DPanoramaImageInline(admin.TabularInline):
    model = Bim6DPanoramaImage
    extra = 1
    verbose_name = "Ảnh 360 độ"
    verbose_name_plural = "Danh sách Ảnh Panorama 360° Trực quan"


# --- 2. CÁC INLINE CHI TIẾT THEO LOẠI DỊCH VỤ ---
class Bim3DDetailInline(admin.StackedInline):
    model = Bim3DDetail
    can_delete = False
    max_num = 1
    verbose_name = "Nội dung chi tiết BIM 3D"
    verbose_name_plural = "CHI TIẾT NỘI DUNG BIM 3D (Áp dụng nếu chọn kiểu BIM 3D)"
    classes = ["collapse"]  # Có thể thu gọn


class DrawingDetailInline(admin.StackedInline):
    model = DrawingDetail
    can_delete = False
    max_num = 1
    verbose_name = "Nội dung Triển khai bản vẽ"
    verbose_name_plural = "CHI TIẾT TRIỂN KHAI BẢN VẼ & TOOL XUNG ĐỘT (Áp dụng nếu chọn Triển khai bản vẽ)"
    classes = ["collapse"]


class Bim5DDetailInline(admin.StackedInline):
    model = Bim5DDetail
    can_delete = False
    max_num = 1
    verbose_name = "Nội dung chi tiết BIM 5D (Khối lượng)"
    verbose_name_plural = (
        "CHI TIẾT NỘI DUNG BIM 5D - KHỐI LƯỢNG (Áp dụng nếu chọn BIM 5D)"
    )
    classes = ["collapse"]


class Bim6DDetailInline(admin.StackedInline):
    model = Bim6DDetail
    can_delete = False
    max_num = 1
    verbose_name = "Nội dung chi tiết BIM 6D (Vận hành)"
    verbose_name_plural = (
        "CHI TIẾT NỘI DUNG BIM 6D - VẬN HÀNH & IFC (Áp dụng nếu chọn BIM 6D)"
    )
    classes = ["collapse"]


# --- 3. ĐĂNG KÝ DUY NHẤT 1 NƠI QUẢN LÝ TẬP TRUNG ---
@admin.register(BimServiceCategory)
class BimServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("order", "name", "layout_type", "is_coming_soon", "is_active")
    list_display_links = ("name",)
    list_editable = ("order", "is_coming_soon", "is_active")
    list_filter = ("layout_type", "is_coming_soon", "is_active")
    search_fields = ("name", "summary")
    prepopulated_fields = {"slug": ("name",)}

    # Nhúng trực tiếp các bảng con vào đây
    inlines = [
        Bim3DDetailInline,
        DrawingDetailInline,
        Bim5DDetailInline,
        Bim6DDetailInline,
    ]

    fieldsets = (
        ("1. THÔNG TIN CƠ BẢN", {"fields": ("name", "slug", "order", "is_active")}),
        (
            "2. HIỂN THỊ TRANG CHỦ & PHÂN LOẠI GIAO DIỆN",
            {
                "description": "Chọn kiểu Layout giao diện tương ứng để hệ thống tự động render trang chi tiết phù hợp.",
                "fields": ("summary", "layout_type", "is_coming_soon"),
            },
        ),
    )


# --- 4. CHO PHÉP UPLOAD ẢNH PHỤ NHANH KHI CẦN ---
# (Các bảng này chỉ đăng ký nếu muốn upload hàng loạt ảnh, còn chi tiết nội dung đã gom hết vào BimServiceCategory)
@admin.register(Bim3DDetail)
class Bim3DDetailStandaloneAdmin(admin.ModelAdmin):
    inlines = [Bim3DImageInline]
    list_display = ("category",)


@admin.register(DrawingDetail)
class DrawingDetailStandaloneAdmin(admin.ModelAdmin):
    inlines = [DrawingFileInline]
    list_display = ("category",)


@admin.register(Bim6DDetail)
class Bim6DDetailStandaloneAdmin(admin.ModelAdmin):
    inlines = [Bim6DPanoramaImageInline]
    list_display = ("category",)
