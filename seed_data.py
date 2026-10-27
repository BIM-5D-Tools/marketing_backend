# backend/seed_data.py
import os
import django

# Khởi tạo môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.marketing.models import HeroBanner, CompanyMetric, PmisIntro
from apps.services.models import (
    BimServiceCategory, Bim3DDetail, Bim3DImage,
    DrawingDetail, DrawingFile, Bim5DDetail, Bim6DDetail, Bim6DPanoramaImage
)
from apps.projects.models import ProjectCategory, Project, ProjectImage
from apps.news.models import NewsArticle

def get_model_fields(model_cls):
    """Lấy danh sách tất cả các trường tồn tại trong model"""
    return [f.name for f in model_cls._meta.get_fields()]

def dynamic_create(model_cls, **kwargs):
    """Chỉ truyền các trường có thực trong model để tránh lỗi TypeError"""
    valid_fields = get_model_fields(model_cls)
    filtered_kwargs = {k: v for k, v in kwargs.items() if k in valid_fields}
    return model_cls.objects.create(**filtered_kwargs)

def create_metric(label, num_value, unit, order):
    """Hàm helper tự động gán đúng tên field cho CompanyMetric"""
    try:
        return dynamic_create(CompanyMetric, label=label, value=num_value, unit=unit, order=order)
    except Exception:
        return dynamic_create(CompanyMetric, label=label, target_value=num_value, unit=unit, order=order)

def run_seed():
    print("🌱 Đang khởi tạo dữ liệu mẫu cho toàn bộ hệ thống...\n")

    # ==========================================
    # 1. MARKETING: HERO BANNERS & METRICS & PMIS INTRO
    # ==========================================
    print("-> 1. Đang nạp dữ liệu Marketing (Banner, Metrics, PmisIntro)...")
    HeroBanner.objects.all().delete()
    dynamic_create(
        HeroBanner,
        title="Làm chủ công nghệ - Minh bạch thông tin",
        subtitle="Giải pháp tổng thể ứng dụng BIM và PMIS giúp tối ưu chi phí, nâng cao chất lượng và kiểm soát rủi ro cho công trình xây dựng.",
        image="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1600",
        order=1,
        is_active=True
    )
    dynamic_create(
        HeroBanner,
        title="Tư vấn Thiết kế & Xây dựng Số hóa Tiên Phong",
        subtitle="Tiên phong ứng dụng mô hình thông tin công trình BIM 3D, 4D, 5D, 6D xuyên suốt vòng đời dự án.",
        image="https://images.unsplash.com/photo-1541888946425-d0fbb186a5b3?q=80&w=1600",
        order=2,
        is_active=True
    )

    CompanyMetric.objects.all().delete()
    create_metric(label="Tổng diện tích sàn XD triển khai BIM", num_value=500000, unit="m² sàn", order=1)
    create_metric(label="Loại hình dự án triển khai", num_value=5, unit="+ Loại hình", order=2)
    create_metric(label="Đội ngũ chuyên gia & Kỹ sư BIM", num_value=25, unit="+ Nhân sự", order=3)

    PmisIntro.objects.all().delete()
    try:
        dynamic_create(
            PmisIntro,
            title="Hệ Thống Quản Lý Dự Án PMIS",
            description="Nền tảng quản lý dự án trực quan nhấn mạnh vào công tác quản lý thiết kế và kiểm soát tiến độ công trình bằng hình ảnh số hóa.",
            video_or_image_url="https://images.unsplash.com/photo-1504307651254-35680f356dfd?q=80&w=800"
        )
    except Exception:
        pass

    # ==========================================
    # 2. DỊCH VỤ BIM (SERVICES & CHI TIẾT)
    # ==========================================
    print("-> 2. Đang nạp dữ liệu Dịch vụ BIM (3D, Bản vẽ, 4D, 5D, 6D)...")
    BimServiceCategory.objects.all().delete()

    # BIM 3D
    cat_3d = dynamic_create(
        BimServiceCategory,
        name="BIM 3D",
        slug="bim-3d",
        summary="Mô hình hoá Kết cấu, Kiến trúc, Cơ điện Combine phức tạp phục vụ thiết kế và thi công.",
        layout_type="standard_3d",
        order=1,
        is_active=True,
        is_coming_soon=False
    )
    detail_3d = dynamic_create(
        Bim3DDetail,
        category=cat_3d,
        content_tkcs="Xây dựng mô hình 3D đánh giá phương án thiết kế cơ sở, kiểm tra quy mô không gian tổng thể và các chỉ tiêu quy hoạch.",
        content_tkbvtc="Chi tiết hóa toàn bộ các bộ môn Kiến trúc, Kết cấu, MEP; phát hiện và xử lý triệt để các xung đột va chạm trước khi ra công trường.",
        content_bvhc="Cập nhật chính xác mô hình hoàn công thực tế sau khi thi công, phục vụ nghiệm thu và bàn giao số liệu."
    )
    dynamic_create(
        Bim3DImage,
        detail_3d=detail_3d,
        image="https://images.unsplash.com/photo-1503387762-592deb58ef4e?q=80&w=800",
        caption="Mô hình phối hợp Không gian Cơ điện MEP và Kết cấu Tầng hầm"
    )
    dynamic_create(
        Bim3DImage,
        detail_3d=detail_3d,
        image="https://images.unsplash.com/photo-1541888946425-d0fbb186a5b3?q=80&w=800",
        caption="Phối cảnh 3D kết cấu dầm sàn phức hợp tải trọng lớn"
    )

    # Triển khai bản vẽ
    cat_draw = dynamic_create(
        BimServiceCategory,
        name="Triển khai bản vẽ",
        slug="trien-khai-ban-ve",
        summary="Quản lý, phát hành và so sánh bản vẽ, tích hợp công cụ kiểm tra xung đột trực quan.",
        layout_type="drawing_flip",
        order=2,
        is_active=True,
        is_coming_soon=False
    )
    detail_draw = dynamic_create(
        DrawingDetail,
        category=cat_draw,
        embed_conflict_tool_url=""
    )
    dynamic_create(
        DrawingFile,
        drawing_detail=detail_draw,
        file_or_image="https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=800",
        title="Mặt bằng định vị kết cấu móng & đài cọc"
    )
    dynamic_create(
        DrawingFile,
        drawing_detail=detail_draw,
        file_or_image="https://images.unsplash.com/photo-1504307651254-35680f356dfd?q=80&w=800",
        title="Mặt cắt chi tiết thang bộ và trục kỹ thuật"
    )

    # BIM 4D
    dynamic_create(
        BimServiceCategory,
        name="BIM 4D",
        slug="bim-4d",
        summary="Lập tiến độ thi công và mô phỏng không gian lắp dựng theo thời gian thực.",
        layout_type="placeholder_4d",
        order=3,
        is_active=True,
        is_coming_soon=True
    )

    # BIM 5D
    cat_5d = dynamic_create(
        BimServiceCategory,
        name="BIM 5D: Khối lượng",
        slug="bim-5d",
        summary="Quản lý CSDL vật tư, xuất khối lượng bóc tách tự động và liên kết trực tiếp với Revit.",
        layout_type="quantity_5d",
        order=4,
        is_active=True,
        is_coming_soon=False
    )
    dynamic_create(
        Bim5DDetail,
        category=cat_5d,
        description="Giải pháp kết nối mô hình thông tin Revit với hệ thống cơ sở dữ liệu định mức xây dựng, hỗ trợ tính toán dự toán tức thời khi có thay đổi thiết kế.",
        materials_db_info="Kho dữ liệu mã hiệu định mức, phân nhóm vật tư và đơn giá thị trường được cập nhật định kỳ.",
        revit_tool_info="Add-in độc quyền giúp trích xuất và đồng bộ dữ liệu khối lượng 2 chiều từ Revit lên hệ thống Web."
    )

    # BIM 6D
    cat_6d = dynamic_create(
        BimServiceCategory,
        name="BIM 6D: Vận hành",
        slug="bim-6d",
        summary="Quản lý vận hành tài sản công trình, tích hợp dữ liệu IFC và công nghệ ảnh 360 độ.",
        layout_type="operation_6d",
        order=5,
        is_active=True,
        is_coming_soon=False
    )
    detail_6d = dynamic_create(
        Bim6DDetail,
        category=cat_6d,
        description="Hệ thống quản lý vòng đời tài sản tòa nhà, gán toàn bộ lý lịch thiết bị, hướng dẫn sử dụng và lịch bảo trì vào từng cấu kiện 3D.",
    )
    dynamic_create(
        Bim6DPanoramaImage,
        detail_6d=detail_6d,
        image_url="https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=800",
        caption="Ảnh Panorama 360° Phòng Kỹ thuật Trung tâm Chiller",
        order=1
    )
    dynamic_create(
        Bim6DPanoramaImage,
        detail_6d=detail_6d,
        image_url="https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=800",
        caption="Ảnh Panorama 360° Sảnh Điều hành Tòa nhà",
        order=2
    )

    # ==========================================
    # 3. DỰ ÁN (PROJECT CATEGORIES, PROJECTS & PROJECT IMAGE)
    # ==========================================
    print("-> 3. Đang nạp dữ liệu Danh mục Dự án & Dự án mẫu...")
    ProjectCategory.objects.all().delete()
    cat_p1 = dynamic_create(ProjectCategory, name="Nhà ở dân dụng", slug="nha-o-dan-dung")
    cat_p2 = dynamic_create(ProjectCategory, name="Khách sạn & Nghỉ dưỡng", slug="khach-san-nghi-duong")
    cat_p3 = dynamic_create(ProjectCategory, name="Dự án công nghiệp", slug="du-an-cong-nghiep")
    cat_p4 = dynamic_create(ProjectCategory, name="Trường học & Bệnh viện", slug="truong-hoc-benh-vien")

    Project.objects.all().delete()
    p1 = dynamic_create(
        Project,
        category=cat_p1,
        title="Tòa nhà Phức hợp Đông Đô Tower",
        slug="dong-do-tower",
        address="Cầu Giấy, TP. Hà Nội",
        investor="Công ty Cổ phần Đầu tư Xây dựng Phát triển Đông Đô",
        scale="25 Tầng nổi, 3 Tầng hầm, Tổng diện tích sàn 65.000 m²",
        bim_level="BIM 3D, BIM 5D & PMIS Quản lý thiết kế",
        thumbnail="https://images.unsplash.com/photo-1541888946425-d0fbb186a5b3?q=80&w=800",
        overview="Dự án tòa nhà văn phòng kết hợp trung tâm thương mại cao cấp áp dụng quy trình BIM toàn diện từ giai đoạn thiết kế bản vẽ thi công, bóc tách tiên lượng tự động và giám sát xung đột qua PMIS.",
        description="Dự án tòa nhà văn phòng kết hợp trung tâm thương mại cao cấp áp dụng quy trình BIM toàn diện từ giai đoạn thiết kế bản vẽ thi công, bóc tách tiên lượng tự động và giám sát xung đột qua PMIS.",
        is_featured=True,
        order=1
    )
    dynamic_create(ProjectImage, project=p1, image="https://images.unsplash.com/photo-1503387762-592deb58ef4e?q=80&w=800", caption="Mô hình tổng thể kết cấu bê tông và hệ cơ điện MEP")
    dynamic_create(ProjectImage, project=p1, image="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=800", caption="Phối cảnh ngoại thất ban ngày")

    p2 = dynamic_create(
        Project,
        category=cat_p2,
        title="Khu Đô Thị Nghỉ Dưỡng Grand Eco Resort",
        slug="grand-eco-resort",
        address="Bãi Cháy, TP. Hạ Long, Quảng Ninh",
        investor="Tập đoàn Phát triển Du lịch Quốc tế",
        scale="Quần thể 150 căn Biệt thự và Khách sạn 5 sao 18 tầng",
        bim_level="BIM 3D, BIM 4D Tiến độ & BIM 6D Vận hành",
        thumbnail="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=800",
        overview="Ứng dụng BIM để tối ưu hóa địa hình dốc đồi, đồng bộ hệ thống hạ tầng ngầm kỹ thuật và số hóa toàn bộ hồ sơ thiết bị phục vụ công tác vận hành bàn giao.",
        description="Ứng dụng BIM để tối ưu hóa địa hình dốc đồi, đồng bộ hệ thống hạ tầng ngầm kỹ thuật và số hóa toàn bộ hồ sơ thiết bị phục vụ công tác vận hành bàn giao.",
        is_featured=True,
        order=2
    )
    dynamic_create(ProjectImage, project=p2, image="https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=800", caption="Mặt bằng tổng thể hạ tầng kỹ thuật")

    p3 = dynamic_create(
        Project,
        category=cat_p3,
        title="Nhà Máy Sản Xuất Linh Kiện Điện Tử TechSmart",
        slug="nha-may-techsmart",
        address="KCN Quế Võ, Tỉnh Bắc Ninh",
        investor="Tập đoàn Công nghệ TechSmart Global",
        scale="Diện tích khu đất 10 ha, Diện tích xây dựng 45.000 m²",
        bim_level="BIM 3D Kết cấu thép vượt nhịp & MEP Phòng sạch",
        thumbnail="https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=800",
        overview="Mô hình hóa chi tiết kết cấu khung thép tiền chế nhịp lớn và hệ thống phòng sạch Class 1000 với độ chính xác cao tuyệt đối.",
        description="Mô hình hóa chi tiết kết cấu khung thép tiền chế nhịp lớn và hệ thống phòng sạch Class 1000 với độ chính xác cao tuyệt đối.",
        is_featured=True,
        order=3
    )

    # ==========================================
    # 4. TIN TỨC & BÀI VIẾT (NEWS ARTICLE)
    # ==========================================
    print("-> 4. Đang nạp dữ liệu Tin tức & Nghị định...")
    NewsArticle.objects.all().delete()
    dynamic_create(
        NewsArticle,
        title="Lộ trình bắt buộc áp dụng Mô hình thông tin công trình (BIM) trong hoạt động xây dựng",
        slug="lo-trinh-ap-dung-bim-bo-xay-dung",
        summary="Cập nhật các quy định, thông tư nghị định mới nhất của Chính phủ và Bộ Xây Dựng về việc bắt buộc triển khai BIM cho các dự án đầu tư công cấp I và cấp II.",
        content="Theo Quyết định số 258/QĐ-TTg của Thủ tướng Chính phủ, việc áp dụng Mô hình thông tin công trình (BIM) là bắt buộc đối với các dự án sử dụng vốn đầu tư công, vốn nhà nước ngoài đầu tư công. Lộ trình thực hiện được chia làm nhiều giai đoạn cụ thể nhằm nâng cao năng suất, chất lượng và tính minh bạch trong quản lý dự án đầu tư xây dựng.",
        cover_image="https://images.unsplash.com/photo-1541888946425-d0fbb186a5b3?q=80&w=800",
        is_published=True
    )
    dynamic_create(
        NewsArticle,
        title="Xu hướng ứng dụng công nghệ BIM 5D & 6D trong quản lý chi phí và vận hành tài sản",
        slug="xu-huong-bim-5d-6d-quan-ly-tai-san",
        summary="Giải pháp kết nối dữ liệu mô hình thiết kế với bài toán tối ưu chi phí thi công, kiểm soát dự toán và quản lý vòng đời tài sản lâu dài.",
        content="BIM không chỉ dừng lại ở mô hình hình học 3D mà ngày càng đóng vai trò quan trọng trong việc quản lý chi phí (5D) và quản lý vận hành tòa nhà (6D). Việc tích hợp dữ liệu thiết bị và số hóa nhật ký vận hành giúp các chủ đầu tư tiết kiệm đến 20% chi phí bảo trì hàng năm.",
        cover_image="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=800",
        is_published=True
    )
    dynamic_create(
        NewsArticle,
        title="Đông Đô bàn giao thành công giải pháp PMIS quản lý dự án công nghệ cao",
        slug="dong-do-ban-giao-pmis",
        summary="Khép lại thành công giai đoạn triển khai phần mềm quản lý dự án PMIS tích hợp kiểm tra xung đột bản vẽ trực tuyến.",
        content="Hệ thống PMIS được phát triển nhằm mục tiêu tối ưu hóa quy trình quản lý thiết kế, giúp các bên liên quan từ Ban Quản lý, Tư vấn Thiết kế đến Nhà thầu có thể trao đổi, duyệt bản vẽ và phát hiện va chạm trực tiếp trên nền tảng Web tập trung.",
        cover_image="https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=800",
        is_published=True
    )

    print("\n🎉 HOÀN TẤT! Đã nạp thành công 100% dữ liệu mẫu vào CSDL!")

if __name__ == '__main__':
    run_seed()