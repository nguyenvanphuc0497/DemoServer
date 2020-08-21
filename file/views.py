import os
from wsgiref.util import FileWrapper

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

from file.forms import DocumentForm


def download_file(request, file_name):
    media_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/media'
    file_path = media_path + '/%s' % file_name
    if os.path.exists(file_path):
        zip_file = open(file_path, 'rb')
        response = HttpResponse(FileWrapper(zip_file), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=%s' % file_name
        return response
    else:
        return HttpResponse("File not found!", status=200)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Upload file success!!!", status=200)
    else:
        form = DocumentForm()
    return render(request, 'file/model_form_upload.html', {
        'form': form
    })
