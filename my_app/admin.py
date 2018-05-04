# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from suit.admin import SortableTabularInline, SortableStackedInline, SortableModelAdmin

from my_app.models import *


@admin.register(Product)
class ProductAdmin(SortableModelAdmin):
    list_display = ('name', 'pub')
    sortable = 'ordering_1'

class LookBookProductInline(SortableStackedInline):
    model = LookBookProduct
    #raw_id_fields = ['product']
    extra = 0
    sortable = 'ordering_3'

class LookBookImageInline(SortableStackedInline):
    model = LookBookImage
    extra = 0
    sortable = 'ordering_4'

@admin.register(LookBook)
class LookBookAdmin(SortableModelAdmin):
    list_display = ('name', 'pub')
    sortable = 'ordering_2'
    inlines = [ LookBookProductInline, LookBookImageInline]
