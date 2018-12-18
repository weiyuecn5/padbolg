from django.shortcuts import render,redirect,reverse
import time
from .models import *
from django.http import HttpResponse

def index(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        cxbh = request.POST.get("cxbh")
        cwbh = request.POST.get("cwbh")
        try:

            if cxbh:
                cxjg = []
                shujuku=Pad.objects.get(pk=cxbh)
                cxjg.append(shujuku)
                return render(request,'jg.html',{'shuju':cxjg})
            elif cwbh:
                cxjg = []
                shujuku=Pad.objects.all()
                for shuju in shujuku:
                    if cwbh in shuju.cwbh:
                        cxjg.append(shuju)
                return render(request,'jg.html',{'shuju':cxjg})
        except:
            return HttpResponse("无数据,请重新查询!")

        return  render(request,'jg.html')

def addshuju(request):
    if request.method == 'GET':
        return render(request,'addshuju.html')
    else:
        zhbh=request.POST.get("zhbh")
        stsl=request.POST.get("stsl")
        cwbh=request.POST.get("cwbh")
        gxsj=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        try:
            shujuku = Pad.objects.get(pk=zhbh)
            shujuku.cwbh=shujuku.cwbh+cwbh+','
            if stsl:
                shujuku.stsl=stsl
            shujuku.gxsj=gxsj
            shujuku.save()
            return HttpResponse('账号:%s 已更新!'%zhbh)
        except:
            shujuku = Pad(zhbh=zhbh, stsl=stsl, cwbh=cwbh+',', gxsj=gxsj)
            shujuku.save()
            return HttpResponse('账号:%s 已加入数据库!'%zhbh)
def delshuju(request,zhid):
    try:
        shujuku=Pad.objects.get(pk=zhid)
        shujuku.delete()
        return HttpResponse('编号:%s 已经删除!'%zhid)
    except:
        return HttpResponse('编号:%s 不存在!'%zhid)