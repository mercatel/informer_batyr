import datetime
import uuid

from django.db import models
from django.urls import reverse

from batyr.models import Legal_entity, Shop


class WorkerStatusCis(models.Model):
    work_status = models.CharField(max_length=48)

    def __str__(self):
        return "%s" % self.work_status

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class WorkerCis(models.Model):
    name = models.CharField(max_length=120, verbose_name="ФИО")
    work_status = models.ForeignKey(WorkerStatusCis, on_delete=models.CASCADE, blank=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Специалист КРО"
        verbose_name_plural = "Специалисты КРО"


class TabInv(models.Model):
    slug = models.SlugField(max_length=120, unique=True, blank=True, default=uuid.uuid4)
    shop = models.CharField(max_length=120, verbose_name="Магазин")
    sv_shop = models.CharField(max_length=100, verbose_name="СВ")
    dm_shop = models.CharField(max_length=100, verbose_name="ДМ")
    date_inv = models.CharField(max_length=120, verbose_name="Дата")
    dm_shop_new = models.CharField(max_length=120, blank=True, default=None, verbose_name="ДМ принимающий")
    res_main = models.DecimalField(max_digits=9, decimal_places=2, default=None, verbose_name="Осн.мето.хр")
    res_defect = models.DecimalField(max_digits=9, decimal_places=2, default=None, verbose_name="Зона Брака")
    res_6_line = models.DecimalField(max_digits=9, decimal_places=2, default=None, verbose_name="Бал. Лок.")
    res_4_line = models.DecimalField(max_digits=9, decimal_places=2, default=None, verbose_name="4 Линия")
    res_total = models.DecimalField(max_digits=9, decimal_places=2, default=None, verbose_name="Итого")
    type_inv = models.CharField(max_length=120, default=None, verbose_name="тип инв")
    format_shop = models.IntegerField(blank=True, default=None, verbose_name="Формат")  # достаем формат с Shop
    fact_format = models.IntegerField(default=None, verbose_name="Формат Факт")
    coment = models.CharField(max_length=120, blank=True, null=True, default=None, verbose_name="Коментарии")
    qky_mop = models.IntegerField(default=None, verbose_name="Кол.Моп")
    fact_qky_mop = models.IntegerField(default=None, verbose_name="Факт.Кол.Моп")
    qky_scro = models.IntegerField(default=None, verbose_name="Кол.СКРО")
    diver_qky_mop = models.IntegerField(default=None, verbose_name="Отклонение")
    vscro = models.CharField(max_length=100, verbose_name="ВСКРО")
    t_o = models.DecimalField(max_digits=15, decimal_places=2, default=None, verbose_name="ТО")
    percent_of_to = models.DecimalField(max_digits=9, decimal_places=2, default=None, verbose_name="% от ТО")
    resort_001 = models.DecimalField(max_digits=9, decimal_places=2, default=None, verbose_name="001 счет")
    previous_date = models.CharField(max_length=40, default=None, verbose_name="Дата пред. инвент")  # АВТОМАТИЗИРОВАТЬ
    time_end = models.CharField(max_length=50, blank=True, default=0, verbose_name="Время окончания инвент")

    class Meta:
        verbose_name = "Таблица инв. СКРО"
        verbose_name_plural = "Таблица инв. СКРО"

    def __str__(self):
        return "%s" % self.shop

    def save(self, *args, **kwargs):
        self.time_end = datetime.datetime.today().strftime("%H:%M")
        self.res_total = self.res_4_line + self.res_6_line + self.res_defect + self.res_main + self.resort_001
        if not self.dm_shop_new:
            self.type_inv = "плановая"
        else:
            self.type_inv = "смена"

        self.diver_qky_mop = self.fact_qky_mop - self.qky_mop
        self.percent_of_to = self.res_total * 100 / self.t_o

        """ подтягиваем формат магазина с дислокации """

        def shop_split_shop_num(shop):  # вытаскиваем №маг в int
            lst = self.shop.split()
            shop_num = int(lst[0])
            return shop_num

        def shop_split_legal_entity(shop):  # вытаскиваем Юр.лицо в id
            lst = self.shop.split()
            legal_entity = str(lst[1])
            legal_entity_id = Legal_entity.objects.get(name=legal_entity).id
            return legal_entity_id

        shop_object = Shop.objects.filter(number_id=shop_split_shop_num(self.shop)).filter(
            legal_entity=shop_split_legal_entity(self.shop))
        shop_get = shop_object.get()
        self.format_shop = shop_get.format

        t = datetime.datetime.now()
        self.slug = str(shop_split_legal_entity(self.shop)) + "-" + str(t.hour) + str(t.minute) + str(t.second)

        super(TabInv, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_tab_invent_url', kwargs={'slug': self.slug})
