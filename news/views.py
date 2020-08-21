import os
from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django.shortcuts import render

from .forms import PostForm, SendEmail


# Create your views here.
def index(request):
    return HttpResponse("xxx")


def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})


def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Luu oke")
        else:
            return HttpResponse("Khong dc validate")
    else:
        return HttpResponse("Khong phai post request")


def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})


def process(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            tieude = m.cleaned_data['title']
            cc = m.cleaned_data['cc']
            noidung = m.cleaned_data['content']
            email = m.cleaned_data['email']
            context = {"tieude": tieude, "cc": cc, "noidung": noidung, "email": email, }
            return render(request, 'news/print_email.html', context)
        else:
            return HttpResponse('form not validate')
    else:
        HttpResponse("Khong phai POST method")


def zip_file(request):
    zip_path = os.path.dirname(os.path.realpath(__file__))
    zip_file = open(zip_path + "/src/game_file.zip", 'rb')
    response = HttpResponse(FileWrapper(zip_file), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'game_file.zip'
    return response
