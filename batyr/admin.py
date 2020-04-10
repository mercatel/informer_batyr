from django.contrib import admin

from batyr.models import Shop, Legal_entity, Supervisor, News, Category, Tag, Comment, CommentCategory


class ShopAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Shop._meta.fields]  # отображение полей

    class Meta:
        model = Shop



admin.site.register(Comment)
admin.site.register(CommentCategory)

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Legal_entity)
admin.site.register(Supervisor)
