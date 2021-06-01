from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    # 어떤 사용자가 어떤 제품을 주문하기에 외래키인 ForeignKey가 필요
    # fcuser안에 있는 Fcuser라는 클래스를 불러온다!
    # ForeignKey를 사용할 때는 on_delete를 꼭 설정해줘야 한다(사용자가 삭제되었을 때 주문 데이터는 어떻게 처리할지)
    # on_delete=models.CASCADE로 설정하게 되면 사용자가 삭제되면 주문 데이터도 같이 삭제된다
    # user = models.ForeignKey(
    #     'common.Fcuser', on_delete=models.CASCADE, verbose_name='사용자')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = 'order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
