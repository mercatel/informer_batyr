import collections
import json

from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
import django_excel as excel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from mk_rc.forms import FormBdVsd
from mk_rc.models import Vsd1C, VsdMerc
from mk_rc.serializers import VsdMercSerializer


def vsd(request):  # добавить фильтр по магазину через Ajax

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


def vsd_filtr(request):
    if request.GET:
        shop = request.GET.get('shop')
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
        data = {}
        count_js = 0
        for item in context:
            count_js += 1
            res = {
                str(count_js): {"shop": str(item[0]),
                                "name1c": str(item[1]),
                                "date": str(item[2]),
                                "quant": str(item[3]),
                                "namemerc": str(item[4])
                                },
            }
            data.update(res)

        context_res = {
            'elements': data,
        }

        return JsonResponse(context_res)
    else:
        pass


def bd_vsd(request):
    # vsd1c = Vsd1C.objects.all()
    # bd_vsd = VsdMerc.objects.all()
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


class ApiVsdMerc(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = None
        self.method = None

    def get(self, request):
        model = VsdMerc.objects.all()
        serializer = VsdMercSerializer(model, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request):
        print(request.data)
        review = VsdMercSerializer(data=request.data)
        if review.is_valid():
            review.save()
        else:
            print('невалидны')

        return Response(status=201)

    def delete(self, request, id_vsd):
        print(id_vsd)
        model = VsdMerc.objects.get(id=id_vsd)
        model.delete()
        return Response(status=204)

    def put(self, request, id_vsd):
        print(request.data)
        model = VsdMerc.objects.get(id=id_vsd)
        serializer = VsdMercSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def details(request, id_vsd):
    print(id_vsd)
    try:
        model = VsdMerc.objects.get(id=id_vsd)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = VsdMercSerializer(model)
        return Response(serializer.data)
    elif request.method == 'PUT':  # Update
        serializer = VsdMercSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update table in DB
            return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        model.delete()
        return Response(status=204)
