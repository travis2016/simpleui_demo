import markdown
from django.db import models
from mdeditor.fields import MDTextField
# Create your models here.


class message(models.Model):
    interfacename = models.CharField(max_length=128, verbose_name='接口名称', unique=True, db_index=True)
    interfaced_esc = models.CharField(max_length=128, verbose_name='接口描述', unique=False, db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '接口信息'
        verbose_name_plural = '接口详细信息'

    def __str__(self):
        return (self.interfacename,self.interfaced_esc)