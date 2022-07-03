from django.views import View, generic
from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .forms import AuthorForm
from .models.ComicModels import Author


class EComicIndexView(generic.TemplateView):
    template_name = "e_comic_home.html"


class EComicCreateView(View):
    def get(self, request, *args, **kwargs):
        """"""
        return render(request, 'e_comic_create.html')

    def post(self, request, *args, **kwargs):
        """"""
        return render(request, 'e_comic_create.html')


# def comic_create(request):
#     form = AuthorForm(request.POST or None)
#     context = {'form': form}
#     if request.method == 'POST' and form.is_valid():
#         post = form.save(commit=False)
#         formset = ComicFormset(request.POST, instance=post)
#         if formset.is_valid():
#             post.save()
#             formset.save()
#             return HttpResponseRedirect('../')
#     else:
#         context['formset'] = ComicFormset()
#         print('ERROR FORM INVALID')
    
#     return render(request, 'e_comic_test.html', context)


def example(request):
    model = Author()
    form = AuthorForm()
    return render(request, "e_comic_test.html", {"form": form, "model": model})
