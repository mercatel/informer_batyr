from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Legal_entity(models.Model):
    """ Юр лицо"""
    name = models.CharField(max_length=120, default=None, verbose_name='Юр.Лицо')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Юр.Лицо"
        verbose_name_plural = "Юр.Лицо"


class Supervisor(models.Model):
    """ Супервайзеры """
    name = models.CharField(max_length=120, default=None, verbose_name='Супервайзер')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Супервайзер"
        verbose_name_plural = "Супервайзеры"


class Shop(models.Model):
    """ Магазины """
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


class Category(models.Model):
    """Класс категорий статей
    """
    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Класс тегов статей
    """
    title = models.CharField("Тег", max_length=50)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title


class News(models.Model):
    """Класс новостей
    """
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    title = models.CharField("Заголовок", max_length=100)
    text_min = RichTextField("Мин. текст", config_name='default')
    text = RichTextUploadingField("Текст статьи", config_name='default')
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    description = models.CharField("Описание", max_length=100)
    keywords = models.CharField("Ключевые слова", max_length=50)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class CommentCategory(models.Model):
    """ Класс категорий комментариев"""
    category = models.CharField('Категория', max_length=240)

    class Meta:
        verbose_name = "Категория комментария"
        verbose_name_plural = "Категории комментариев"

    def __str__(self):
        return self.category


class Comment(models.Model):
    """ Клас комментариев"""
    category_comment = models.ForeignKey(CommentCategory, verbose_name="Категория комментариев", on_delete=models.SET_NULL,
                                         null=True)
    comment_txt = models.TextField()
    comment_create = models.DateTimeField("Дата комментария", auto_now_add=True)
    comment_check = models.BooleanField('Прочитаны', default=False)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return str(self.category_comment) + " - " +  str(self.comment_check)


