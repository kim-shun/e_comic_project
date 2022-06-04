from django.shortcuts import render
from django.views import generic


class EComicDisp(generic.TemplateView):
  template_name = "e_comic_home.html"
