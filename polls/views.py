from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


# Create your views here.


def index(request):
    my_name = "Phuc Nguyen"
    tai_san = ["Dien thoai", "Xe May", "Tien"]
    context = {"name": my_name, "tai_san": tai_san}
    return render(request, "polls/index.html", context)


def view_list(request):
    list_question = Question.objects.all()
    context = {"list_quest": list_question}
    return render(request, "polls/question_list.html", context)


def detail_view(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"question": q})


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST["choice"]
        c = q.choice_set.get(pk=data)
    except:
        return HttpResponse("Loi khong co data")
    c.vote += 1
    c.save()
    return render(request, "polls/result.html", {"q": q})
