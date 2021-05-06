from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import QuestionForm, AnswerForm
from .models import Question, Answer


def index(request):
    page = request.GET.get('page', '1')
    # DB 기본 정렬 : ASC. -를 붙이면 역순으로 정렬.
    question_list = Question.objects.order_by('-create_date')
    # 1page당 10개의 게시물을 가져옴.
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    #context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user    # 추가한 속성 author 적용
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    # question.answer_set.create(content=request.POST.get('cont'), create_date=timezone.now())

    # 다른 방법
    # answer = Answer(question=question, content=request.POST.get('cont'), create_date=timezone.now())
    # answer.save()
    # ---------------------------------- [edit] ---------------------------------- #
    # return redirect('pybo:detail', question_id=question.id)
    # ---------------------------------------------------------------------------- #


@login_required(login_url='common:login')
def question_create(request):
    # form = QuestionForm()
    # return render(request, 'pybo/question_form.html', {'form': form})
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user  # 추가한 속성 author 적용
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}

    return render(request, 'pybo/question_form.html', context)

