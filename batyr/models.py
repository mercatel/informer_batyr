from django.db import models


class Legal_entity(models.Model):
    name = models.CharField(max_length=120, default=None, verbose_name='Юр.Лицо')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Юр.Лицо"
        verbose_name_plural = "Юр.Лицо"


class Supervisor(models.Model):
    name = models.CharField(max_length=120, default=None, verbose_name='Супервайзер')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Супервайзер"
        verbose_name_plural = "Супервайзеры"


class Shop(models.Model):
    number_id = models.IntegerField(blank=True, verbose_name='№ маг.')
    legal_entity = models.ForeignKey(Legal_entity, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                     verbose_name='Юр.Лицо')
    address = models.CharField(max_length=120, blank=True, verbose_name='Адрес')
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, blank=True, null=True, default=None,
                                   verbose_name='Супервайзер')
    format = models.IntegerField(blank=True, verbose_name='Формат')

    def __str__(self):
        return "%s %s" % (self.number_id, self.legal_entity)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
