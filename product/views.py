from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import FormView

# from product.forms import RegisterForm, ProductForm
from product.forms import ProductForm
from product.models import Product


def index(request):
    """
    product 목록 출력
    """
    page = request.GET.get('page', '1')
    product_list = Product.objects.order_by('-created')
    paginator = Paginator(product_list, 6)
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


# class ProductCreate(FormView):
#     template_name = 'product/product_register.html'
#     form_class = RegisterForm
#     success_url = '/product/'


# class ProductModify(FormView):
#     template_name = 'product/product_register.html'
#     form_class = RegisterForm
#     success_url = '/product/'


@login_required(login_url='common:login')
def product_create(request):
    """
    product 등록
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product:index')
    else:
        form = ProductForm()
    context = {'form': form}

    return render(request, 'product/product_register.html', context)


@login_required(login_url='common:login')
def product_modify(request, product_id):
    """
    product 수정
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product:detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'product/product_register.html', context)


@login_required(login_url='common:login')
def product_delete(request, product_id):
    """
    product 삭제
    """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('product:index')


def search(request):
    """
    product 검색
    """
    products = None
    keyword = None

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        products = Product.objects.all().filter(name__contains=keyword)

    context = {
        'products': products, 'keyword': keyword,
    }

    return render(request, 'product/search.html', context)
