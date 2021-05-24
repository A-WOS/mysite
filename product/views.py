from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from product.forms import RegisterForm
from product.models import Product


def index(request):
    """
    product 목록 출력
    """
    page = request.GET.get('page', '1')
    product_list = Product.objects.order_by('-created')
    paginator = Paginator(product_list, 10)
    page_obj = paginator.get_page(page)
    context = {'product_list': page_obj}
    # context = {'product_list': product_list}

    return render(request, 'product/product_list.html', context)


def detail(request, product_id):
    """
    product 내용 출력
    """
    # product = Product.objects.get(id=product_id)
    # Product.objects.get(id=product_id)
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}

    return render(request, 'product/product_detail.html', context)


# @method_decorator(admin_required, name='dispatch')
# @method_decorator(name='dispatch')
# class ProductRegister(FormView):
#     template_name = "product/register.html"
#     form_class = RegisterForm
#     success_url = '/product/'
#
#     def form_valid(self, form):
#         product = Product(
#             name=form.data.get('name'),
#             price=form.data.get('price'),
#             description=form.data.get('description'),
#             stock = form.data.get('stock')
#         )
#         product.save()
#         return super().form_valid(form)
