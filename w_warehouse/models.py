from django.db import models


# Create your models here.


class WarehouseType(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=64, verbose_name='仓库类型名称')

    class Meta:
        db_table = 'w_wharehouse_type'
        verbose_name = '仓库类型'
        verbose_name_plural = '仓库类型'

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='主键')
    wh_no = models.CharField(max_length=64, verbose_name='仓库编号')
    wh_name = models.CharField(max_length=1024, verbose_name='仓库名')
    wh_type = models.ForeignKey(WarehouseType, on_delete=models.SET_NULL, verbose_name='仓库类型', null=True)
    principal = models.CharField(max_length=64, verbose_name='负责人')
    phone_no = models.CharField(max_length=64, verbose_name='联系电话')
    address = models.CharField(max_length=64, default=None, verbose_name='地址')
    status = models.BooleanField(verbose_name='合作状态')
    start_date = models.DateField(blank=True, verbose_name='合作时间')
    end_date = models.DateField(blank=True, verbose_name='终止合作时间', null=True)
    memo = models.CharField(max_length=128, verbose_name='备注', null=True)

    class Meta:
        db_table = 'w_wharehouse'
        verbose_name = '仓库信息'
        verbose_name_plural = '仓库信息'
        # ordering = ['start_date']

