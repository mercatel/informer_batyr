from django.shortcuts import get_object_or_404, render


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


def get_slug_last(model):  # достает последний абсолютный урл
    slug_obj = model.objects.latest('id')
    slag = slug_obj.get_absolute_url()
    print(slug_obj)
    return slag


class ObjectSearchMixin:
    model = None
    template = None

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, context={'model': obj})
