from django.contrib import admin

from mk.models import WorkerStatusCis, WorkerCis, CheckListMK


class CheckListMKAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CheckListMK._meta.fields]  # отображение полей
    exclude = ['slug']  # исключение полей
    list_filter = ["shop"]  # фильтр по полю
    search_fields = [field.name for field in CheckListMK._meta.fields] # добовляем поле поиска

    class Meta:
        model = CheckListMK


admin.site.register(CheckListMK, CheckListMKAdmin)  # регистрируем модель в админке


admin.site.register(WorkerStatusCis)
admin.site.register(WorkerCis)
