from django.db import models


class Vsd1C(models.Model):
    shop = models.CharField(max_length=20)
    name_1c = models.CharField(max_length=124, blank=True)
    data_1c = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Отбор с 1С"
        verbose_name_plural = "Отбор с 1С"


class VsdMerc(models.Model):
    name_1c = models.CharField(max_length=128, blank=True, verbose_name='Наименование 1С')
    name_merc = models.CharField(max_length=128, blank=True, verbose_name='Наименование Меркурий')
    w_in_pack = models.DecimalField(max_digits=10, decimal_places=3, blank=True, verbose_name='Вес упаковки')

    class Meta:
        verbose_name = "БД Меркурий"
        verbose_name_plural = "БД Меркурий"
