from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *


def import_data():
    pass


def export_data():
    pass


import_data.short_description = "导入数据"
export_data.short_description = "导出数据"


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    actions = [import_data, export_data]
    list_per_page = 10
    actions_on_top = True
    list_display = ['wh_no', 'wh_name', 'wh_type', 'principal', 'status', 'start_date', 'end_date']


admin.site.register(WarehouseType)
