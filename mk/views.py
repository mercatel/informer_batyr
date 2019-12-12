from operator import attrgetter, itemgetter

from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.views import View

from batyr.models import Supervisor
from mk.forms import CheckListMkForm
from mk.models import CheckListMK
from mk.utils import ObjectDetailMixin, get_slug_last, ObjectSearchMixin


class ChecklistView(ObjectDetailMixin, View):
    model = CheckListMK
    template = 'views_report_mk/check_list_view.html'


def form_check_list_mk(request):
    form = CheckListMkForm(request.POST or None)

    if request.method == "POST" and form.is_valid():  # Если получаем данные с формы Анкеты

        shop = form.cleaned_data["shop"]
        sv_shop = form.cleaned_data["sv_shop"]
        dm_shop = form.cleaned_data["dm_shop"]
        skkro = form.cleaned_data["skkro"]

        new_form = form.save()

        return redirect(get_slug_last(CheckListMK))

        # Сделать переход к тестированию

    return render(request, 'form_mk/check_list_mk.html', locals())


class MkReport(ObjectSearchMixin, View):
    model = CheckListMK
    template = 'views_report_mk/mk_report.html'


class MkReportEtc(ObjectSearchMixin, View):
    model = CheckListMK
    template = 'views_report_mk/mk_etc_report.html'


def mk_nkro_report(request):
    obj = CheckListMK.objects.all()
    sv = Supervisor.objects.all()
    data = {}
    data_shop = {}
    #
    # По ДМ.................................................
    #
    for item_shop in obj:
        shop = item_shop.shop
        shop_obj = CheckListMK.objects.filter(shop=shop)
        sum_scu = 0
        sum_p2_1 = 0
        sum_summ = 0
        sum_dis_price = 0
        sum_lack_price = 0
        sum_etc = 0
        for item_re_shop in shop_obj:
            sum_scu += item_re_shop.sku
            sum_p2_1 += item_re_shop.p2_1
            sum_summ += item_re_shop.p2_sum
            sum_dis_price += item_re_shop.dis_price
            sum_lack_price += item_re_shop.lack_price
            sum_etc += item_re_shop.etc

        res_shop = {
            shop: {"dm": item_shop.dm_shop, "address": item_shop.address_shop,
                   "Date": item_shop.date, "sv": item_shop.sv_shop, "sum_scu": sum_scu,
                   "sum_p2_1": sum_p2_1, "sum_summ": sum_summ, "sum_dis_price": sum_dis_price,
                   "sum_lack_price": sum_lack_price, "sum_etc": sum_etc},
        }

        data_shop.update(res_shop)

    #
    # по СВ.........................................
    #

    for item_sv in sv:
        filter_sv = obj.filter(sv_shop=item_sv)
        sku = 0
        p2_1 = 0
        p2_sum = 0
        lack_price = 0
        dis_price = 0
        etc = 0

        for item_report in filter_sv:
            sku += int(item_report.sku)
            p2_1 += int(item_report.p2_1)
            p2_sum += item_report.p2_sum
            lack_price += int(item_report.lack_price)
            dis_price += int(item_report.dis_price)
            etc += item_report.etc

        res = {
            item_sv: {"sku": sku, "p2_1": p2_1, "p2_sum": p2_sum, "lack_price": lack_price, "dis_price": dis_price,
                      "etc": etc},
        }
        data.update(res)

    return render(request, 'views_report_mk/mk_nkro_report.html',
                  context={'model': obj, 'data': data, 'data_by_dm': data_shop})


def search_shop(request):
    if request.GET:
        shop = request.GET.get('shop')
        sv = request.GET.get('sv')
        res_search = CheckListMK.objects.filter(shop__contains=shop, sv_shop__contains=sv).values()

        context = {
            'elements': list(res_search)
        }

        return JsonResponse(context)
    else:
        pass


def search_date(request):
    data_sv = []
    data_shop = []
    data_shop_dict = {}

    if request.GET:
        start = request.GET.get('start')
        end = request.GET.get('end')
        obj = CheckListMK.objects.filter(date__range=(start, end))

        # отчет по ДМ**********************
        for item_shop in obj:
            shop = item_shop.shop
            shop_obj = CheckListMK.objects.filter(shop=shop, date__range=(start, end))
            sum_scu = 0
            sum_p2_1 = 0
            sum_summ = 0
            sum_dis_price = 0
            sum_lack_price = 0
            sum_etc = 0
            for item_re_shop in shop_obj:
                sum_scu += item_re_shop.sku
                sum_p2_1 += item_re_shop.p2_1
                sum_summ += item_re_shop.p2_sum
                sum_dis_price += item_re_shop.dis_price
                sum_lack_price += item_re_shop.lack_price
                sum_etc += item_re_shop.etc

            res_shop = {
                shop: {"shop": str(shop), "dm": str(item_shop.dm_shop), "address": str(item_shop.address_shop),
                       "date": str(item_shop.date), "sv": str(item_shop.sv_shop), "sum_scu": str(sum_scu),
                       "sum_p2_1": str(sum_p2_1), "sum_summ": str(sum_summ),
                       "sum_dis_price": str(sum_dis_price),
                       "sum_lack_price": str(sum_lack_price), "sum_etc": str(sum_etc)
                       }, }
            data_shop_dict.update(res_shop)

        for key, val in data_shop_dict.items():
            data_shop.append(val)

        # Отчет по СВ******************************
        sv = Supervisor.objects.all()
        itog_sku = 0
        for item_sv in sv:
            filter_sv = obj.filter(sv_shop=item_sv)
            count = 1
            sku = 0
            p2_1 = 0
            p2_sum = 0
            lack_price = 0
            dis_price = 0
            etc = 0
            itog_sku += sku

            for item_report in filter_sv:
                count += 1
                sku += int(item_report.sku)
                p2_1 += int(item_report.p2_1)
                p2_sum += item_report.p2_sum
                lack_price += int(item_report.lack_price)
                dis_price += int(item_report.dis_price)
                etc += item_report.etc

            res = {"sv": str(item_sv), "sku": str(sku), "p2_1": str(p2_1), "p2_sum": str(p2_sum),
                   "lack_price": str(lack_price),
                   "dis_price": str(dis_price),
                   "etc": str(etc),
                   }
            data_sv.append(res)

        context = {
            'onsv': list(data_sv),
            'ondm': list(data_shop),
        }

        return JsonResponse(context)
    else:
        pass
