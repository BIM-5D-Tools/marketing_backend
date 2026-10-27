from django.db import models


# Create your models here.
class ContactRequest(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Họ và tên")
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=255, blank=True)
    message = models.TextField(verbose_name="Nội dung lời nhắn")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Thông tin Liên hệ"
        verbose_name_plural = "Danh sách Khách hàng Liên hệ"
