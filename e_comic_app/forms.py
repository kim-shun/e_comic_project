from django import forms
from .models.ComicModels import Author


# class NewUserForm(forms.ModelForm):
#     class Meta():
#         model = Author
#         fields = '__all__'

# class NewComicForm(forms.ModelForm):
#     class Meta():
#         model = Comic
#         fields = ('comic_name',)

# CreateComicFormset = forms.inlineformset_factory(
#     Author, Comic, fields=('comic_name', 'author_1', 'author_2', 'author_3', 'remarks'),
#     extra=1, can_delete=False
# )

# class NewComicForm(forms.ModelForm):
#     class Meta():
#         model = Comic
#         fields = ('comic_name',)


class AuthorForm(forms.ModelForm):
    class Meta():
        model = Author
        fields = ('author',)


# # ComicFormset = forms.inlineformset_factory(
# #      Author, Comic, fields='__all__',
# #      extra=1, can_delete=False
# # )

# ComicFormset = forms.inlineformset_factory(
#      Author, Comic, fields=('comic_score', 'remarks', 'author_1'),
#      extra=1, can_delete=False
# )
