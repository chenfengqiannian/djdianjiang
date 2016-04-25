#coding:utf-8
from django.shortcuts import render
import json
from dianjiangapp.models import user,gongcheng,tupianclass,shezhi
from django.http.response import HttpResponseNotFound, HttpResponseNotAllowed,HttpResponseForbidden,HttpResponse,JsonResponse
from dianjiangapp.form import AddForm
from _ast import IsNot
from time import timezone

# Create your views here.

def myprint(ni):
    print ni
    return

def objecttodict(mlist,fields):
    jsonre=[]
    
    for mobject in mlist:
       
        js={}
        for l in fields:
            if(hasattr(mobject,l)):
                js[l]=getattr(mobject,l)
        jsonre.append(js)
    return jsonre
    



def userinapi(request):
    try:
        if request.method == 'POST':
            
            data = json.loads(request.body)
            myprint(data)
            dataphone=data['phone']
            leixing=data.get('leixing','-1')
            if(leixing=='0'):
                if(user.objects.get(phone=data['phone']).userpw==data['userpw']):
                    return HttpResponse("ok")
                else:
                    return HttpResponseForbidden()
            if(leixing=='1'):
                if(len(user.objects.filter(phone=data['phone']))>=1):
                    return HttpResponseForbidden()
                else:
                    mydidian=data['didianchar']
                    myuser=user.objects.create(phone=data['phone'],userpw=data['userpw'],didianchar=mydidian,job=data["job"])
                    
                    #myuser.didianchar.add(mydidian)
                    return HttpResponse('ok')
            if(leixing=='2'):
                userpwxiugai=user.objects.get(phone=data['phone'])
                if (userpwxiugai.userpw==data['olduserpw']):
                    userpwxiugai.userpw=data['newuserpw']    
                    userpwxiugai.save()
                    return HttpResponse('ok')
                else:
                    return HttpResponseForbidden()
            if(leixing=='3'):
                userzhufubao=user.objects.get(phone=data['phone'])
                userzhufubao.zhifubaozhanghao=data['zhifubaozhaohao']
                userzhufubao.save()
                return HttpResponse('ok')
                
            
            
            
            clphone=user.objects.get(phone=dataphone)
            reqkey=data.keys()
            
            for k in reqkey:
                setattr(clphone,k,data[k])
            clphone.save()
            return HttpResponse("ok")
        if request.method == 'GET':
            jsonmap={}
            
            myjob=request.GET.get('job',-1)
            
            
            if(myjob!=-1):
                userl=user.objects.filter(job=myjob)
                jsonlistout=[]
                for muser in userl:
                    jsonmap={}
            
            
            
            
                    fields=muser._meta.get_all_field_names()
                    
                    for l in fields:
                        
                        if(hasattr(muser,l) and l!='userpw'):
                            jsonmap[l]=getattr(muser,l)
                    
                    
                    
                    
                    
                    gongchengs=muser.gongcheng_set.all()
            
                    
                    gongchenglist=[]
                    for object in gongchengs:
                        fields=object._meta.get_all_field_names()
                        gongchengdict={}
                        for k in fields:
                            
                            if(hasattr(object,k) and k!='reship'):
                                
                                    
                                gongchengdict[k]=getattr(object,k)
                                if(k=='autotime'):
    
                                    gongchengdict['autotime']=object.autotime.strftime("%Y-%m-%d %H:%M:%S")
                                if(k=='kaishitime' or k=='jieshutime'):
                                    gongchengdict[k]=getattr(object,k).strftime("%Y-%m-%d")
                                    
                                
                        gongchenglist.append(gongchengdict)
                    
                    myprint(gongchenglist)
                    
                    
                    jsonmap['gongcheng_set']=gongchenglist
                    jsonlistout.append(jsonmap)
                    
                    
                
            
                
                
                
                
            else:
            
            
            
            
            
            
                
                
                mphone=request.GET['phone']
                
                
               
                muser=user.objects.get(phone=mphone)
                   
                
                
                
                
                jsonout={}
                
                
                
                
                fields=muser._meta.get_all_field_names()
                
                for l in fields:
                    if(hasattr(muser,l) and l!='userpw'):
                        jsonmap[l]=getattr(muser,l)
                
                
                
                
                
                gongchengs=muser.gongcheng_set.all()
        
                
                gongchenglist=[]
                for object in gongchengs:
                    fields=object._meta.get_all_field_names()
                    gongchengdict={}
                    for k in fields:
                        if(hasattr(object,k) and k!='reship'):
                            
                                
                            gongchengdict[k]=getattr(object,k)
                            if(k=='autotime'):
                                gongchengdict['autotime']=object.autotime.strftime("%Y-%m-%d %H:%M:%S")
                            if(k=='kaishitime' or k=='jieshutime'):
                                    gongchengdict[k]=getattr(object,k).strftime("%Y-%m-%d")
                    gongchenglist.append(gongchengdict)
                
                myprint(gongchenglist)
                
                
                jsonmap['gongcheng_set']=gongchenglist
               
                    
                
                
                
                
                
                
                
                
                myprint (jsonmap)
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            if(myjob!=-1):
                myprint (jsonlistout)
                return HttpResponse(json.dumps(jsonlistout))
            else:
                return JsonResponse(jsonmap)
            
    except Exception, e:
            myprint (e)
        
             
def imageup(request):
    if request.method == 'POST':
        try:
            form = AddForm(request.POST,request.FILES)
        # check whether it's valid:
        
            #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            myid= request.POST.get("id",-1)
            myshangchuan=request.POST.get('shangchuan',-1)
            listshangchuang=myshangchuan.split(',')
                
            if id == -1 and myshangchuan==-1:
                return  HttpResponseNotAllowed
            dj=[]
            dataimagelist=[]
                #headImg = form.cleaned_data['formimage']
                
            dataimagelist=form.files.values()
                
                #mtupianclass=tupianclass.objects.create(tupianshuju=headImg)
                #mtupiandata=mtupianclass.tupianshuju
                
            if(listshangchuang[0]=='user'):
                muser=user.objects.get(phone=myid)
                mlist=getattr(muser,listshangchuang[1])
                for datafromlist in dataimagelist:
                    mtupianclass=tupianclass.objects.create(tupianshuju=datafromlist)
                    mlist.append(mtupianclass.tupianshuju.name)
                muser.save()
            if(listshangchuang[0]=='gongcheng'):
                mgongcheng=gongcheng.objects.get(id=myid)
                mlist=getattr(mgongcheng,listshangchuang[1])
                    
                for datafromlist in dataimagelist:
                    mtupianclass=tupianclass.objects.create(tupianshuju=datafromlist)
                    mlist.append(mtupianclass.tupianshuju.name)
                        
                mgongcheng.save()

                
            return HttpResponse('ok')
                    
        except Exception, e:
            myprint (e)
            myprint (request)
            return HttpResponseNotAllowed(e)
              
    if request.method == 'GET':
        form = AddForm()

        return render(request,'post.html', {'form': form})      
def gongchengapi(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            leixing=data.get('leixing',-1)
            if(leixing=='0'):
                mphone=data['phone']
                muser=user.objects.get(phone=mphone)
                mgongcheng=gongcheng()
                reqkey=data.keys()
                
                for k in reqkey:
                    if(hasattr(mgongcheng,k)):
                        setattr(mgongcheng,k,data[k])
                mgongcheng.save()
                mgongcheng.reship.add(muser)
                
                
                return HttpResponse(mgongcheng.id)
            else:
                mid=data['id']
                
                mgongcheng=gongcheng.objects.get(id=mid)
                reqkey=data.keys()
                for k in reqkey:
                    if(hasattr(mgongcheng,k)):
                        setattr(mgongcheng,k,data[k])
                mgongcheng.save()
                return HttpResponse('ok')
        if request.method == 'GET':
            
            gongchengs=gongcheng.objects.all()
            gongchenglist=[]
            fields=gongchengs[0]._meta.get_all_field_names()
            for object in gongchengs:
                gongchengdict={}
                for k in fields:
                    if(hasattr(object,k)):
                        if(k=='reship'):
                            gongchengdict['gongchenggj']=objecttodict(object.reship.filter(job=0),['phone','touxiang','gongzhong','xingming','dengji','rixin'])
                            gongchengdict['gongcengdj']=objecttodict(object.reship.filter(job=1),['phone','touxiang','gongzhong','xingming','dengji','rixin'])
                            continue
                        
                        gongchengdict[k]=getattr(object,k)
                        if(k=='autotime'):
                            gongchengdict['autotime']=object.autotime.strftime("%Y-%m-%d %H:%M:%S")
                        if(k=='kaishitime' or k=='jieshutime'):
                                    gongchengdict[k]=getattr(object,k).strftime("%Y-%m-%d")
                gongchenglist.append(gongchengdict)
                
    
            
            
            return JsonResponse(gongchenglist,safe=False)
    except Exception, e:
            myprint (e)
            
def shezhiapi(request):
    try:
        mapout={}
        lis=shezhi.objects.all()
        for ob in lis:
            
            neirong=[]
            neirong.append(ob.neirong)
            neirong.append(ob.tupian.name)
            mapout[ob.name]=neirong
            
        
        return JsonResponse(mapout,safe=False)
        
    except Exception,e:
            myprint (e)        
        
        