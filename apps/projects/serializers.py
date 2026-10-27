from rest_framework import serializers
from .models import ProjectCategory, Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "caption"]


class ProjectListSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "thumbnail",
            "address",
            "investor",
            "category_name",
            "is_featured",
        ]


class ProjectDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    gallery = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "thumbnail",
            "address",
            "investor",
            "overview",
            "category_name",
            "gallery",
        ]


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = "__all__"
