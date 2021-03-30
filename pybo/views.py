from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    # DB 기본 정렬 : ASC. -를 붙이면 역순으로 정렬.
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
