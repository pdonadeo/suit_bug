# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Max


class TsModel(models.Model):
    class Meta:
        abstract = True
    ts_insert = models.DateTimeField(auto_now_add=True)
    ts = models.DateTimeField(auto_now=True)

class Product(TsModel):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['ordering_1',]

    ordering_1 = models.PositiveIntegerField()
    pub = models.BooleanField(default=True)
    name = models.CharField(max_length=1024, unique=True)

    def __unicode__(self):
        return self.name

class LookBook(TsModel):
    class Meta:
        verbose_name = 'LookBook'
        verbose_name_plural = 'LookBooks'
        ordering = ['ordering_2',]

    ordering_2 = models.PositiveIntegerField()
    pub = models.BooleanField(default=True)
    name = models.CharField(max_length=1024, unique=True)

class LookBookProduct(TsModel):
    class Meta:
        verbose_name = 'Product in LookBook'
        verbose_name_plural = 'Products in LookBooks'
        ordering = ['ordering_3',]
        unique_together = ['lookbook', 'product']

    ordering_3 = models.PositiveIntegerField()
    pub = models.BooleanField(default=True)
    lookbook = models.ForeignKey(LookBook)
    product = models.ForeignKey(Product)

    def __unicode__(self):
        return self.product.name

class LookBookImage(TsModel):
    class Meta:
        verbose_name = 'LookBook image'
        verbose_name_plural = 'LookBook images'
        ordering = ['ordering_4',]

    lookbook = models.ForeignKey(LookBook)
    ordering_4 = models.PositiveIntegerField()
    pub = models.BooleanField(default=True)
    desc = models.CharField(max_length=1024, null=True, blank=True)

    def __unicode__(self):
        return 'LookBook image'
