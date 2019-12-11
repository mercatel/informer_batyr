from django import forms
from django.forms import Textarea

from batyr.models import Supervisor, Shop
from mk.models import CheckListMK, WorkerCis


class CheckListMkForm(forms.ModelForm):
    skkro = forms.ModelChoiceField(queryset=WorkerCis.objects.filter(work_status_id=1))
    sv_shop = forms.ModelChoiceField(queryset=Supervisor.objects.all())
    shop = forms.ModelChoiceField(queryset=Shop.objects.all())

    class Meta:
        model = CheckListMK
        exclude = ["shop_num", "address_shop", "date", "sku",
                   "dis_price", "lack_price",
                   "etc"]

        widgets = {
            'p1_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p1_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p1_3comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p2_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p2_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p3_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p4_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p5_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p5_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p5_3comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p6_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p6_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p6_2_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p6_3comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p6_4comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p7_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p7_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p7_3comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p7_4comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p8_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p8_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p8_3comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p8_4comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p8_5comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p8_6comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p8_7comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_3comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_4comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_3comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_4comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_5comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_6comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_7comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_8comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_5_9comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_6comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_7comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p9_8comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p10_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p11_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p11_2comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p11_3comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p11_4comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p11_5comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p11_6comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p11_7comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'p12_1comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'service_ing_comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'service_log_comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'service_it_comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'pr_comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'contract_department_comment': Textarea(attrs={'cols': 40, 'rows': 1}),
            'subarenda_comment': Textarea(attrs={'cols': 40, 'rows': 1}),
        }
