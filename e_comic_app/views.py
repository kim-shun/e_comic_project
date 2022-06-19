from django.views import View, generic
from django.shortcuts import render


class EComicIndexView(generic.TemplateView):
    template_name = "e_comic_home.html"


class EComicCreateView(View):
    def get(self, request, *args, **kwargs):
        """"""
        return render(request, 'e_comic_create.html')

    def post(self, request, *args, **kwargs):
        """"""
        return render(request, 'e_comic_create.html')
