from django import forms

from mk_rc.models import VsdMerc


class FormBdVsd(forms.ModelForm):
    class Meta:
        model = VsdMerc

        fields = ["name_1c", "name_merc", "w_in_pack"]
        exclude = []
