from django.http import HttpResponse


def index(request):
    return HttpResponse("smartshop에 오신 것을 환영합니다.")

