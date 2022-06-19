from django.db import models
# from django.core.validators import MaxValueValidator


class Author(models.Model):
    author = models.CharField(verbose_name="作者", max_length=70, null=False, unique=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)


class Comic(models.Model):
    comic_name = models.CharField(verbose_name="漫画名", max_length=100, null=False, unique=True)
    author_1 = models.ForeignKey(Author, verbose_name="作者1", max_length=70, null=True, related_name="re_author_1", on_delete=models.PROTECT)
    author_2 = models.ForeignKey(Author, verbose_name="作者2", max_length=70, null=True, related_name="re_author_1", on_delete=models.PROTECT)
    author_3 = models.ForeignKey(Author, verbose_name="作者3", max_length=70, null=True, related_name="re_author_1", on_delete=models.PROTECT)
    author_4 = models.ForeignKey(Author, verbose_name="作者4", max_length=70, null=True, related_name="re_author_1", on_delete=models.PROTECT)
    remarks = models.CharField(verbose_name="備考", max_length=200, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)


# class ComicEvaluation(models.Model):
#     comic_name = models.ForeignKey(Comic, verbose_name="漫画名", to_field="comic_name", db_column="comic_name",
#                                    related_name="c_names", max_length=128, null=False, on_delete=models.PROTECT)
#     comic_score = models.PositiveSmallIntegerField(verbose_name="評点", validators=[MaxValueValidator(100)], null=False)
#     comment = models.TextField(verbose_name="コメント", null=True)
#     nickname = models.ForeignKey(to_field="nickname", verbose_name="作成者", db_column="created_by", max_length=100,
#                                  null=True, on_delete=models.PROTECT)
#     created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)


# class ComicEvaluationDetail(models.Model):
#     comic_name = models.ForeignKey(Comic, verbose_name="漫画名", to_field="comic_name", db_column="comic_name",
#                                    related_name="c_names_detail", max_length=128, null=False, on_delete=models.PROTECT)
#     evaluation_item_id = models.PositiveSmallIntegerField(verbose_name="評価項目ID", null=False)
#     item_content = models.CharField(verbose_name="評価項目内容", max_length=50, null=True)
#     created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
