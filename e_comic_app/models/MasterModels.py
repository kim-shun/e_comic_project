from django.db import models


class MSelectName(models.Model):
    """選択肢マスタ"""
    select_id = models.CharField(verbose_name="選択肢ID", max_length=10, unique=True, index=True, null=False)
    select_name = models.CharField(verbose_name="選択肢名称", max_length=50, null=False)

    class Meta:
        # テーブル名
        db_table = 'm_select_name'


class MSelectItem(models.Model):
    "選択肢項目マスタ"
    kind_id = models.CharField(verbose_name="種別ID", max_length=10, null=False)
    item_id = models.CharField(verbose_name="項目ID", max_length=10, null=False)
    item_name = models.CharField(verbose_name="項目名", max_length=50, null=False)
    order = models.SmallIntegerField(verbose_name="順序", null=False)
    select_id = models.ForeignKey(MSelectName, verbose_name="選択肢ID", to_field='select_id', db_column='select_id',
                                  related_name='re_select_id', on_delete=models.PROTECT, null=False)

    class Meta:
        # テーブル名
        db_table = 'm_select_item'
        # ユニーク制約
        constraints = [
            models.UniqueConstraint(fields=['fc_id', 'item_id', 'select_id', 'order'],
                                    name='u_m_select_item'),
        ]
        # インデックス
        indexes = [
            models.Index(fields=['fc_id', 'item_id', 'select_id', 'order'], name='idx_m_select_item')
        ]


class MLabelName(models.Model):
    """ラベル名称マスタ"""
    label_id = models.CharField(verbose_name="ラベルID", max_length=10, unique=True, index=True, null=False)
    label_name = models.CharField(verbose_name="ラベル名", max_length=50, null=False)

    class Meta:
        # テーブル名
        db_table = 'm_label_name'


class MLabelHierarchy(models.Model):
    """ラベル階層マスタ"""
    label_id = models.ForeignKey(MLabelName, verbose_name="ラベルID", to_field='label_id', db_column='label_id',
                                 related_name='re_label_id', on_delete=models.PROTECT, null=False)
    order = models.SmallIntegerField(verbose_name="順序", null=False)
    parent_label_id = models.ForeignKey(MLabelName, verbose_name="親階層ラベルID", to_field='label_id', db_column='parent_label_id',
                                        related_name='re_parent_label_id', on_delete=models.PROTECT, null=True)

    class Meta:
        # テーブル名
        db_table = 'm_label_deps'
        # ユニーク制約
        constraints = [
            models.UniqueConstraint(fields=['label_id', 'order'], name='u_m_label_hierarchy'),
        ]
        # インデックス
        indexes = [
            models.Index(fields=['parent_label_id', 'order'], name='idx_m_label_hierarchy')
        ]
