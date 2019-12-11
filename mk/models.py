import datetime
import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

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
        verbose_name = "Специалист ККРО"
        verbose_name_plural = "Специалисты ККРО"

def gen_slug(s, d):
    new_slug1 = slugify(s, allow_unicode=True)
    new_slug2 = slugify(d, allow_unicode=True)
    return new_slug1 + '-' + new_slug2


class CheckListMK(models.Model):
    shop = models.CharField(max_length=48, verbose_name="Магазин")  # достаем № маг с Shop
    slug = models.SlugField(max_length=120, unique=True, blank=True, default=uuid.uuid4)
    address_shop = models.CharField(max_length=120, verbose_name="Адрес")
    date = models.DateField(auto_now_add=True, auto_now=False, verbose_name='Дата')
    skkro = models.CharField(max_length=100, verbose_name="СККРО")
    sv_shop = models.CharField(max_length=100, verbose_name="СВ")
    dm_shop = models.CharField(max_length=100, verbose_name="ДМ")

    # 1. Проверка прилегающей территории и входной группы.
    p1_1 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Про-ка прил. тер-рии")
    p1_1comment = models.TextField(max_length=150, blank=True, default=None)
    # ____________________________________________________
    p1_2 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Сан. сост-ие  вход. группы")
    p1_2comment = models.TextField(blank=True, default=None)
    # _____________________________________________________

    p1_3 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Нал-ие значка о запрете курения")
    p1_3comment = models.TextField(blank=True, default=None)

    # _________________________________________________________
    # 2. Реализация товара с истекшим сроком годности
    p2_1 = models.IntegerField(blank=True, null=True, default=0,
                               verbose_name="Просрочка")
    p2_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    p2_2 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Работа с Браком")
    p2_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    p2_sum = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0,
                                 verbose_name="Сумма просрочки:")
    # 3. Реализация бракованного товара (характер брака)
    p3_1 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Брак в ТЗ")
    p3_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    # 4 Не насыщенная выкладка товара
    p4_1 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Отс-вие товара (в ТЗ) OOS")
    p4_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    # 5. Отсутствие ценников
    p5_1 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Отс-вие ценников")
    p5_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p5_2 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Отс-вие ценников на акционный товар")
    p5_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p5_3 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Не соот-вие ценника")
    p5_3comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    # 6. Нарушений правил продажи алкоголя и табачной продукции
    p6_1 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Отс-вие акцизной марки")
    p6_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p6_2 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Не соот-вие ценников на алкоголь и табачную продукцию")
    p6_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p6_2_2 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Отс-вие ценников на алкоголь и табачную продукцию")
    p6_2_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p6_3 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Док-ты на алк.")
    p6_3comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p6_4 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Приемка алк продукции в программе ЕГАИС.")
    p6_4comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    # 7. Наличие очередей
    p7_1 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Более 5 покупателей")
    p7_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p7_2 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Обс-ние по любимой карте")
    p7_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p7_3 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Обс-ние по подарочной карте")
    p7_3comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p7_4 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="алгоритм обс-ния")
    p7_4comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    # 8.  Отсутствие обязательной информации для покупателей о товаре
    p8_1 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="без даты выработки")
    p8_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p8_2 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="без маркиров. ярлыка")
    p8_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p8_3 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="без сроков реал-ции")
    p8_3comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p8_4 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="без этикет-ценника")
    p8_4comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p8_5 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="без перевода на рус. язык")
    p8_5comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p8_6 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="не соот-вие обязательной инфо.")
    p8_6comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p8_7 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="не соб-ние сроков фас. вес. товара")
    p8_7comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    # 9. Нарушение требований санитарных норм и правил:
    p9_1 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Не соб-ние ротации")
    p9_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_2 = models.IntegerField(blank=True, null=True, default=None, verbose_name="товарное соседство")
    p9_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_3 = models.IntegerField(blank=True, null=True, default=None, verbose_name="t-режима")
    p9_3comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_4 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Хранение товара")
    p9_4comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Сан. сос-ние инвентаря")
    p9_5comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_1 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Наличие гигрометров")
    p9_5_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_2 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Наличие дез. раствора")
    p9_5_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_3 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Наличие разделочных досок, ножей")
    p9_5_3comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_4 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Наличие раздевалок с местом хранения спецодежды")
    p9_5_4comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_5 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Проверка холодильного оборудования на его заполнение и санитарное состояние.")
    p9_5_5comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_6 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Заполнение мусорных баков, урн магазина, своевременный вывоз мусора")
    p9_5_6comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_7 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Проверка КПП")
    p9_5_7comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_8 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Проверка правил продажи горячего хлеба")
    p9_5_8comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_5_9 = models.IntegerField(blank=True, null=True, default=None,
                                 verbose_name="Проверка продажи весовой рыбы")
    p9_5_9comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_6 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Наличие листа отметок проведенных влажных уборок.")
    p9_6comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_7 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Отсутствие зона брака в подс. помещении")
    p9_7comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p9_8 = models.IntegerField(blank=True, null=True, default=None,
                               verbose_name="Внешний вид сотрудников")
    p9_8comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    # 10. Проверка медицинских книжек сотрудников.
    p10_1 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name="Проверка мед. книжек")
    p10_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    # 11. Ведение журналов
    p11_1 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name="Ведение журнала сроков годности товара (отсутствует, ведется/не ведется).")
    p11_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p11_2 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name="Ведение бракеражного журнала (отсутствует, ведется/не ведется).")
    p11_2comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p11_3 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name="Ведение журнала контроля температурного режима и влажности в холодильном оборудования  (отсутствует, ведется/не ведется).")
    p11_3comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p11_4 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name="Наличие ППК")
    p11_4comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p11_5 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name="отсутствие обязательной информации на стенде")
    p11_5comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    p11_6 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name="Ведение книги отзывов и предложений. Наличие ответа ДМ на отзывы покупателей.")
    p11_6comment = models.TextField(blank=True, default=None)
    # ____________________________________________________
    p11_7 = models.IntegerField(blank=True, null=True, default=None,
                                verbose_name="Ведение журнала дератизации и дезинсекции.")
    p11_7comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    # 12. Прочее:
    p12_1 = models.IntegerField(blank=True, null=True, default=None, verbose_name="Прочее:")
    p12_1comment = models.TextField(blank=True, default=None)
    # ____________________________________________________

    # Служба Главного Инженера
    service_ing = models.IntegerField(blank=True, null=True, default=None, verbose_name="Сл.Гл.Инженера:")
    service_ing_comment = models.TextField(blank=True, default=None)
    # Служба Логистика
    service_log = models.IntegerField(blank=True, null=True, default=None, verbose_name="Сл.Логист:")
    service_log_comment = models.TextField(blank=True, default=None)
    # СИТ
    service_it = models.IntegerField(blank=True, null=True, default=None, verbose_name="СИТ:")
    service_it_comment = models.TextField(blank=True, default=None)
    # Реклама и PR
    pr = models.IntegerField(blank=True, null=True, default=None, verbose_name="Реклама и PR:")
    pr_comment = models.TextField(blank=True, default=None)
    # Договорной отдел
    contract_department = models.IntegerField(blank=True, null=True, default=None, verbose_name="Договорной отдел:")
    contract_department_comment = models.TextField(blank=True, default=None)
    # 6.1. Субаренда
    subarenda = models.IntegerField(blank=True, null=True, default=None, verbose_name="Субаренда:")
    subarenda_comment = models.TextField(blank=True, default=None)

    # Служба Торговли
    sku = models.IntegerField(blank=True, null=True, default=0, verbose_name="Баллы")

    # Прочее
    etc = models.IntegerField(blank=True, null=True, default=0, verbose_name="Прочее")
    dis_price = models.IntegerField(blank=True, null=True, default=0, verbose_name="Несоответствие ценников")
    lack_price = models.IntegerField(blank=True, null=True, default=0, verbose_name="Отсутствие ценников")
    logging = models.IntegerField(blank=True, null=True, default=None, verbose_name="Ведение журналов")

    class Meta:
        verbose_name = "Чек лист МК"
        verbose_name_plural = "Чек лист МК"

    def __str__(self):
        return str(self.shop)

    def save(self, *args, **kwargs):
        """ массив для SKU, считаем  SKU """
        array = [self.p1_1, self.p1_2, self.p1_3, self.p2_1, self.p2_2, self.p3_1, self.p4_1, self.p5_1, self.p5_2,
                 self.p5_3, self.p6_1, self.p6_2, self.p6_2_2,
                 self.p6_3, self.p6_3, self.p6_4, self.p7_1, self.p7_2, self.p7_3, self.p7_4, self.p8_1, self.p8_2,
                 self.p8_3, self.p8_4, self.p8_5, self.p8_6,
                 self.p8_7, self.p9_1, self.p9_2, self.p9_3, self.p9_4, self.p9_5, self.p9_5_1, self.p9_5_2,
                 self.p9_5_3,
                 self.p9_5_4, self.p9_5_5,
                 self.p9_5_6, self.p9_5_7, self.p9_5_8, self.p9_5_9, self.p9_6, self.p9_7, self.p9_8, self.p10_1,
                 self.p11_1, self.p11_2, self.p11_3,
                 self.p11_4, self.p11_5, self.p11_6, self.p11_7, self.p12_1]

        self.sku = 0

        for p in array:
            if p is None:
                self.sku += 0
            else:
                self.sku += p

        """ массив для "Журналов", считаем  "Журналы" """
        array = [self.p11_1, self.p11_2, self.p11_3, self.p11_6, self.p11_7]
        self.logging = 0
        for p in array:
            if p is None:
                self.logging += 0
            else:
                self.logging += p

        """ массив для "Несоответствие ценников", считаем  "Несоответствие ценников" """
        array = [self.p5_3, self.p6_2]
        self.dis_price = 0
        for p in array:
            if p is None:
                self.dis_price += 0
            else:
                self.dis_price += p
        """ массив для "Отсутствие ценников", считаем  "Отсутствие ценников" """
        array = [self.p5_1, self.p5_2, self.p6_2_2]
        self.lack_price = 0
        for p in array:
            if p is None:
                self.lack_price += 0
            else:
                self.lack_price += p
        """ считаем  "Прочее" """
        if self.p2_1 is None:
            self.etc = self.sku - self.dis_price - self.lack_price
        else:
            self.etc = self.sku - self.p2_1 - self.dis_price - self.lack_price

        """ подтягиваем адрес магазина с дислокации """

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
        self.address_shop = shop_get.address

        """ слаг для чек-листа состоит из №маг-час минуты секунды """
        t = datetime.datetime.now()
        self.slug = str(shop_split_legal_entity(self.shop)) + "-" + str(t.hour) + str(t.minute) + str(t.second)

        super(CheckListMK, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_checklist_url', kwargs={'slug': self.slug})
