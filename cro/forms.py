from django import forms

from batyr.models import Supervisor, Shop
from cro.models import TabInv, WorkerCis


class TableInvForm(forms.ModelForm):
    vscro = forms.ModelChoiceField(queryset=WorkerCis.objects.filter(work_status_id=1), label="ВСКРО")
    sv_shop = forms.ModelChoiceField(queryset=Supervisor.objects.all(), label="Супервайзер")
    shop = forms.ModelChoiceField(queryset=Shop.objects.all(), label="Магазин")

    class Meta:
        model = TabInv

        fields = ["sv_shop", "shop", "date_inv", "dm_shop", "dm_shop_new", "res_main", "res_defect", "res_6_line",
                  "res_4_line", "resort_001", "t_o", "vscro", "qky_scro", "fact_qky_mop", "qky_mop", "previous_date",
                  "fact_format"]
        exclude = ["slug", "format_shop", "res_total", "type_inv", "percent_of_to", "diver_qky_mop", "coment", "time_end"]
