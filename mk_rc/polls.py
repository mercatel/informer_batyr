from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django import forms
import django_excel as excel

from mk_rc.models import Vsd1C


class UploadFileForm(forms.Form):
    file = forms.FileField()


# Create your views here.
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'polls/upload_form.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })


def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        clean_1c = Vsd1C.objects.all()
        clean_1c.delete()
        if form.is_valid():
            request.FILES['file'].save_to_database(
                #name_columns_by_row=-1,
                model=Vsd1C,
                mapdict=['shop', 'name_1c', 'data_1c'])
            return HttpResponseRedirect("/")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, 'polls/upload_form.html')


def exchange(request, file_type):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        filehandle = request.FILES['file']
        return excel.make_response(filehandle.get_sheet(), file_type)
    else:
        return HttpResponseBadRequest()
