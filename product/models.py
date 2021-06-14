from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # image를 텍스트 필드로 한 이유는 좀더 아름답게 만들기 위해서 (summernote 이용)
    image = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    # image = models.ImageField(upload_to="product", blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "상품"
        verbose_name_plural = "상품"
