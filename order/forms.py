from django import forms

from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'product']
        labels = {'quantity': '수량', 'product': '상품'}

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

        if not (quantity and product and user):
            self.add_error('quantity', "수량이 없습니다.")
            self.add_error('product', "상품이 없습니다.")
