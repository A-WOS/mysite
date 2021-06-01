from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
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

    return render(request, 'product/product_detail2.html', context)


class ProductCreate(FormView):
    template_name = 'product/product_register.html'
    form_class = RegisterForm
    success_url = '/product/'


@login_required(login_url='common:login')
def product_delete(request, product_id):
    """
    product 삭제
    """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('product:index')


# @login_required(login_url='common:login')
# def product_modify(request, product_id):
#     """
#     product 수정
#     """
#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == "POST":
#
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('pybo:detail', question_id=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
#     context = {'answer': answer, 'form': form}
#     return render(request, 'pybo/answer_form.html', context)