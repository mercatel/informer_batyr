import collections

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
import django_excel as excel

from mk_rc.forms import FormBdVsd
from mk_rc.models import Vsd1C, VsdMerc


def vsd(request):  # добавить фильтр по магазину через Ajax
    if request.GET:
        shop = request.GET.get('shop')
    else:
        shop = ""
    context = []
    for item in Vsd1C.objects.filter(shop__contains=shop):
        shop = item.shop
        name1c = item.name_1c
        data = item.data_1c
        count = 0
        name_merc = "ищем в ручную"
        quantity = 0

        for item in VsdMerc.objects.filter(name_1c=name1c):
            name_merc = item.name_merc
            quantity = item.w_in_pack

        for item1 in Vsd1C.objects.filter(shop=shop, name_1c=name1c, data_1c=data):
            count += 1

        if quantity == 0:
            quant = "???"
        else:
            quant = count * quantity

        res = [shop, name1c, data, quant, name_merc]

        if res in context:
            pass
        else:
            context.append(res)
    return render(request, 'vsd.html', locals())


def bd_vsd(request):
    vsd1c = Vsd1C.objects.all()
    bd_vsd = VsdMerc.objects.all()
    return render(request, 'bdvsd.html', locals())


def form_bd_vsd(request):
    form = FormBdVsd(request.POST or None)

    if request.method == "POST" and form.is_valid():
        name_1c = form.cleaned_data["name_1c"]
        name_merc = form.cleaned_data["name_merc"]
        w_in_pack = form.cleaned_data["w_in_pack"]

        new_form = form.save()
        return HttpResponseRedirect("/mk_rc/bd_vsd/")

    return render(request, 'forms/formbdvsd.html', locals())


def edit_bd_vsd(request, id):
    try:
        form = VsdMerc.objects.get(id=id)

        if request.method == "POST":
            form.name_1c = request.POST.get("name_1c")
            form.name_merc = request.POST.get("name_merc")
            form.w_in_pack = request.POST.get("w_in_pack")
            new_form = form.save()
            return HttpResponseRedirect("/mk_rc/bd_vsd/")
        else:
            return render(request, "forms/edit.html", locals())
    except VsdMerc.DoesNotExist:
        return HttpResponseNotFound("<h2>Error</h2>")


def delete_bd_vsd(request, id):
    try:
        form = VsdMerc.objects.get(id=id)
        form.delete()
        return HttpResponseRedirect("/mk_rc/bd_vsd/")
    except VsdMerc.DoesNotExist:
        return HttpResponseNotFound("<h2>Error</h2>")
