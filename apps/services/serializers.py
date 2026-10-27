from rest_framework import serializers
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


# --- 1. BIM 3D Serializers ---
class Bim3DImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bim3DImage
        fields = ["id", "image", "caption"]


class Bim3DDetailSerializer(serializers.ModelSerializer):
    images = Bim3DImageSerializer(many=True, read_only=True)

    class Meta:
        model = Bim3DDetail
        fields = ["content_tkcs", "content_tkbvtc", "content_bvhc", "images"]


# --- 2. Triển khai Bản vẽ Serializers ---
class DrawingFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrawingFile
        fields = ["id", "file_or_image", "title"]


class DrawingDetailSerializer(serializers.ModelSerializer):
    drawings = DrawingFileSerializer(many=True, read_only=True)

    class Meta:
        model = DrawingDetail
        fields = ["embed_conflict_tool_url", "drawings"]


# --- 3. BIM 5D & 6D Serializers ---
class Bim5DDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bim5DDetail
        fields = ["description", "video_url", "materials_db_info", "revit_tool_info"]


class Bim6DPanoramaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bim6DPanoramaImage
        fields = ["id", "image_url", "caption", "order"]


class Bim6DDetailSerializer(serializers.ModelSerializer):
    panorama_images = Bim6DPanoramaImageSerializer(many=True, read_only=True)

    class Meta:
        model = Bim6DDetail
        fields = ["description", "video_url", "ifc_file", "panorama_images"]


# --- 4. Main Service Category Serializer (Tự đóng gói Detail tương ứng với Layout) ---
class BimServiceCategorySerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()

    class Meta:
        model = BimServiceCategory
        fields = [
            "id",
            "name",
            "slug",
            "summary",
            "order",
            "layout_type",
            "is_active",
            "is_coming_soon",
            "detail",
        ]

    def get_detail(self, obj):
        # Trả về dữ liệu chi tiết tùy thuộc vào layout_type
        if obj.layout_type == "standard_3d" and hasattr(obj, "detail_3d"):
            return Bim3DDetailSerializer(obj.detail_3d).data
        elif obj.layout_type == "drawing_flip" and hasattr(obj, "detail_drawing"):
            return DrawingDetailSerializer(obj.detail_drawing).data
        elif obj.layout_type == "quantity_5d" and hasattr(obj, "detail_5d"):
            return Bim5DDetailSerializer(obj.detail_5d).data
        elif obj.layout_type == "operation_6d" and hasattr(obj, "detail_6d"):
            return Bim6DDetailSerializer(obj.detail_6d).data
        return None
