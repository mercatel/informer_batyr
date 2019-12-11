from django.contrib import admin

from cro.models import WorkerStatusCis, WorkerCis, TabInv


class TabInvAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TabInv._meta.fields]  # отображение полей
    exclude = ('slug',)  # исключение полей
    list_filter = ["shop"]  # фильтр по полю
    search_fields = [field.name for field in TabInv._meta.fields]  # добовляем поле поиска

    class Meta:
        model = TabInv



admin.site.register(TabInv, TabInvAdmin)  # регистрируем модель в админке

admin.site.register(WorkerStatusCis)
admin.site.register(WorkerCis)
