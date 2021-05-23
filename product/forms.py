from django import forms


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
    stock = forms.IntegerField(
        error_messages={
            'required': "재고를 입력해주세요."
        }, label="재고"
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        if not (name and price and description and stock):
            self.add_error('stock', '모든 값을 입력해야 합니다.')
