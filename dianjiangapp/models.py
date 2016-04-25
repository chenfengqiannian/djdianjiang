#coding:utf-8
from django.db import models
from fields import ListField

import md5
from django.template.defaultfilters import default

m = md5.new()
# Create your models here.



class    user(models.Model):
    phone = models.CharField(u'手机',max_length=255)
    userpw = models.CharField(u'密码',max_length=255)
    
    job=models.BooleanField(u'工匠or点匠,true,false',default=False)
    didianchar=models.CharField(u"地点",max_length=255)
    touxiang=ListField(u'头像',blank=True)
    nichang=models.CharField(u'昵称',max_length=255,blank=True)
    zhifubaozhanghao = models.CharField(u'支付宝账号',max_length=255,blank=True)
    zhanghuyue=models.FloatField(u'账户余额',default=0.0)
    shenfengzhengid=models.CharField(u'身份证',max_length=255,blank=True)
    shenfengzheng=ListField(u'身份证',blank=True)
    xingming=models.CharField(u'姓名',max_length=255,blank=True)
    gongzhong=models.CharField(u'工种',max_length=255,blank=True)
    gongzuodi=models.CharField(u'工作地',max_length=255,blank=True)
    biaoqian=models.CharField(u'标签',max_length=255,blank=True)
    gongsi=models.CharField(u'公司',max_length=255,blank=True) 
    dizhi=models.CharField(u'地址',max_length=255,blank=True)
    ziwojieshao=models.CharField(u'自我介绍',max_length=255,blank=True)
    
    zhengshu=ListField(u'证书',blank=True)
    dengji=models.IntegerField(u'等级',default=0)
    jingyanzhi=models.IntegerField(u'经验值',default=0)
    rixin=models.IntegerField(u'日薪',default=0)
    shouzhijilu=ListField(u'收支记录',blank=True)
    pingjiaxingji=models.FloatField('评级',default=0.0)
    def __unicode__(self):
        
        return self.phone
    
    
    
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        mi=self.userpw.__str__()
        
        if (len(mi)==32):
            self.userpw=mi
        else:
               
            m.update(mi)
    
            
            self.userpw=m.hexdigest()
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
    
    
    
    
class gongcheng(models.Model):

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if(self.pingjiaxingji!=0.0):
            if(self.reship!=None):
                listr=self.reship.filter(job=True)
            
            
            for objectd in listr:
                objectd.pingjiaxingji=((len(objectd.gongcheng_set.all())-1)*objectd.pingjiaxingji+self.pingjiaxingji)/(len(objectd.gongcheng_set.all()))       
                objectd.save()
        
        return models.Model.save(self, force_insert, force_update, using, update_fields)


    

    
    biaoti   = models.CharField(u'标题',max_length=255,blank=True)  
    miaoshu   = models.CharField(u'描述',max_length=255,blank=True) 
    suozaidi   = models.CharField(u'所在地',max_length=255,blank=True) 
    beizhu=models.CharField(u'备注',max_length=255,blank=True)
    xiangxidizhi   = models.CharField(u'详细地址',max_length=255,blank=True)
    tupian=ListField(u'图',blank=True)
    gongzhong=  models.CharField(u'工种',max_length=255,blank=True)    
    yaoqiu=  models.CharField(u'要求',max_length=255,blank=True)
    xinchou=  models.IntegerField(u'薪酬',default=0)
    
    zhuangtaichoices=((-3,u'未发布工程'),(-2,u'删除'),(-1,u'审核失败'),(0,u'审核中'),(1,u'待签合同'),(2,u'招标中'),(3,u'待付款'),(4,u'正在施工'),(5,u'工程完成待付尾款'),(6,u'完成'))
    zhuangtai=models.IntegerField(u'状态',choices=zhuangtaichoices,default=0)
    gongchengjindu=models.TextField(u'工程进度',blank=True)
    yaoqing=ListField(u'邀请列表',blank=True)
    
    pingjia=models.CharField(u'评价',max_length=255,blank=True)
    pingjiatu=ListField(u'评价图',blank=True)
    pingjiaxingji=models.FloatField(u'评价星级',default=0.0)


    fapiaomingcheng=models.CharField(u'发票名称',max_length=255,blank=True)
    fapiaotaitou=models.CharField(u'发票抬头',max_length=255,blank=True)
    fapiaoyouzheng=models.CharField(u'发票邮政编码',max_length=255,blank=True)
    fapiaoshoujian=models.CharField(u'发票收件人',max_length=255,blank=True)
    fapiaodizhi=models.CharField(u'发票地址',max_length=255,blank=True)
    fapiaojisongshijian=models.CharField(u'发票寄送时间',max_length=255,blank=True)
    fapiaojine=models.CharField(u'发票金额',max_length=255,blank=True)
    zhiding=ListField(u'指定',blank=True)
    reship=models.ManyToManyField(user,blank=True)

    autotime=models.DateTimeField(auto_now=True)
    kaishitime=models.DateField(auto_now_add=True)
    jieshutime=models.DateField(auto_now_add=True)
  
    def __unicode__(self):
        
        return self.biaoti






class tupianclass(models.Model):
    tupianshuju=models.ImageField(upload_to='images',max_length=255)
    def __unicode__(self):
        
        return self.id
class shezhi(models.Model):
    name=models.CharField(max_length=255)
    neirong=models.TextField(u'内容',blank=True)
    tupian=models.ImageField(u'设置图片',upload_to='images',max_length=255,blank=True)
    def __unicode__(self):
        
        return self.name
    
    

    