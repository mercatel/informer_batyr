from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from cro.forms import TableInvForm
from cro.models import TabInv
from cro.utils import ObjectDetailMixin, ObjectSearchMixin, get_slug_last


def form_table_inv(request):
    form = TableInvForm(request.POST or None)

    if request.method == "POST" and form.is_valid():  # Если получаем данные с формы Анкеты

        sv_shop = form.cleaned_data["sv_shop"]
        shop = form.cleaned_data["shop"]
        date_inv = form.cleaned_data["date_inv"]
        dm_shop = form.cleaned_data["dm_shop"]
        dm_shop_new = form.cleaned_data["dm_shop_new"]
        res_main = form.cleaned_data["res_main"]
        res_defect = form.cleaned_data["res_defect"]
        res_6_line = form.cleaned_data["res_6_line"]
        res_4_line = form.cleaned_data["res_4_line"]
        resort_001 = form.cleaned_data["resort_001"]
        t_o = form.cleaned_data["t_o"]
        previous_date = form.cleaned_data["previous_date"]
        vscro = form.cleaned_data["vscro"]
        qky_scro = form.cleaned_data["qky_scro"]
        fact_qky_mop = form.cleaned_data["fact_qky_mop"]
        qky_mop = form.cleaned_data["qky_mop"]
        fact_format = form.cleaned_data["fact_format"]

        new_form = form.save()

        return redirect(get_slug_last(TabInv))

    return render(request, 'form_cro/table_invent.html', locals())


class TabInvView(ObjectDetailMixin, View):
    model = TabInv
    template = 'views_report_cro/tab_invent_view.html'


class InventStatsReport(ObjectSearchMixin, View):
    model = TabInv
    template = 'views_report_cro/invent_stat_report.html'


class InventResultReport(ObjectSearchMixin, View):
    model = TabInv
    template = 'views_report_cro/invent_result_report.html'


def search_shop(request):
    if request.GET:
        shop = request.GET.get('shop')
        res_search = TabInv.objects.filter(shop__contains=shop).values()
        context = {
            'elements': list(res_search)
        }
        return JsonResponse(context)
    else:
        pass
