# from django.shortcuts import render, get_object_or_404
# from product.models import Product
#
#
# def index(request):
#     """
#     shop 목록 출력
#     """
#     # page = request.GET.get('page', '1')
#     product_list = Product.objects.order_by('-created')
#     # paginator = Paginator(product_list, 10)
#     # page_obj = paginator.get_page(page)
#     # context = {'product_list': page_obj}
#     context = {'product_list': product_list}
#
#     return render(request, 'product/product_list.html', context)
#
#
# def detail(request, product_id):
#     """
#     shop 내용 출력
#     """
#     # product = Product.objects.get(id=product_id)
#     # Product.objects.get(id=product_id)
#     product = get_object_or_404(Product, pk=product_id)
#     context = {'product': product}
#
#     return render(request, 'product/product_detail.html', context)


