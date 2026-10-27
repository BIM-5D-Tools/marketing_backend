from django.contrib import admin
from .models import HeroBanner, CompanyMetric, PmisIntro


@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")


@admin.register(CompanyMetric)
class CompanyMetricAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "unit", "order")


admin.site.register(PmisIntro)
