from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, redirect

from order.forms import OrderForm
from order.models import Order
from product.models import Product


def index(request):
    """
    order 목록 출력
    """
    page = request.GET.get('page', '1')
    order_list = Order.objects.order_by('-created')
    paginator = Paginator(order_list, 10)
    page_obj = paginator.get_page(page)
    context = {'order_list': page_obj}
    # context = {'product_list': product_list}

    return render(request, 'order/order_list.html', context)


@login_required(login_url='common:login')
def order_create(request):
    """
    order 주문
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                prod = Product.objects.get(pk=form.data.get('product'))
                order = Order(
                    quantity=form.data.get('quantity'),
                    product=prod,
                    user=User.objects.get(email=request.session.get('user'))
                )
                order.save()

                prod.stock -= int(form.data.get('quantity'))
                prod.save()
        return redirect('product:index')
    else:
        form = OrderForm
    context = {'form': form}
    return render(request, 'product/product_list.html', context)
