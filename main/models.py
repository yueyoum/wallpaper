# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Device(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    device = models.CharField(max_length=255, blank=True)
    app_id = models.IntegerField(db_index=True)
    first_login = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(db_index=True)

    class Meta:
        db_table = 'device'
        ordering = ['-last_login']
        verbose_name = '设备'
        verbose_name_plural = '设备'

class Category(models.Model):
    id = models.Integer(primary_key=True)
    name = models.CharField(max_length=32)
    hide_for_review = models.BooleanField(default=False)

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = '分类'

class AppConfig(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='App ID')
    categories = models.CommaSeparatedIntegerField(verbose_name='包含的分类ID列表')
    recommand_category = models.IntegerField(verbose_name='推荐分类')

    version = models.IntegerField(verbose_name='当前版本')

    class Meta:
        db_table = 'app_config'
        verbose_name = '应用设置'
        verbose_name_plural = '应用设置'


class WallPaper(models.Model):
    origin_platform = models.CharField(max_length=64, blank=True)
    category = models.IntegerField(db_index=True)

    width = models.IntegerField()
    height = models.IntegerField()
    key = models.CharField(unique=True)

    add_at = models.DateTimeField(auto_now_add=True, db_index=True)
    hot = models.IntegerField(default=0, db_index=True)

    class Meta:
        db_table = 'wallpaper'
        verbose_name = 'WallPaper'
        verbose_name_plural = 'WallPaper'

