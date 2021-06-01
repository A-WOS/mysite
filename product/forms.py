from django import forms

from product.models import Product


class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '상품명을 입력해주세요.'
        }, label="상품명", max_length=64)

    price = forms.IntegerField(
        error_messages={
            'required': "상품 가격을 입력해주세요."
        }, label="상품 가격",
    )
    description = forms.CharField(
        error_messages={
            'required': "상품 설명을 입력해주세요."
        }, label="상품 설명"
    )
    image = forms.CharField(
        error_messages={
            'required': "상품 이미지를 넣어주세요."
        }, label="상품 이미지"
    )
    stock = forms.IntegerField(
        error_messages={
            'required': "재고를 입력해주세요."
        }, label="재고"
    )

    # validate
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        image = cleaned_data.get('image')
        stock = cleaned_data.get('stock')

        if name and price and description and image and stock:
            product = Product(
                name=name,
                price=price,
                description=description,
                image=image,
                stock=stock
            )
            product.save()
