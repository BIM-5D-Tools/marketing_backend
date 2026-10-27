from rest_framework import serializers
from .models import HeroBanner, CompanyMetric, PmisIntro


class HeroBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroBanner
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if instance.image:
            image_str = str(instance.image)
            if image_str.startswith("http://") or image_str.startswith("https://"):
                ret["image"] = image_str
        return ret


class CompanyMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyMetric
        fields = "__all__"


class PmisIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = PmisIntro
        fields = "__all__"
