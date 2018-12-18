from django.db import models
import django.utils.timezone as timezone
class Pad(models.Model):
    '''
    账号编号: zhbh
    石头数量: stsl
    宠物编号: cwbh
    更新时间: gxsj
    '''
    zhbh = models.CharField(max_length=100,primary_key=True)
    stsl = models.CharField(max_length=100,blank=True)
    cwbh = models.TextField()
    gxsj = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.zhbh