from rest_framework import serializers

from mk_rc.models import Vsd1C, VsdMerc


class VsdMercSerializer(serializers.ModelSerializer):
    class Meta:
        model = VsdMerc
        fields = (
            'id',
            'name_1c',
            'name_merc',
            'w_in_pack'
        )
