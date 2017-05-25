# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 组织考试
class exam(models.Model):
    exam_id = models.CharField(primary_key=True,max_length=32)
    examname = models.TextField()
    topicid = models.CharField(max_length=32)
    groupid = models.CharField(max_length=32)
    begintime = models.CharField(max_length=30)
    begintime = models.CharField(max_length=30)
    endtime = models.CharField(max_length=30)




# 考生信息
class examinee(models.Model):
    userid = models.CharField(max_length=30,primary_key=True)  
    username = models.CharField(max_length=30)
    ticketnumber = models.CharField(max_length=30)
    idcard = models.CharField(max_length=18)
    password = models.CharField(max_length=1000)
    actstatus = models.CharField(max_length=32) # '1: 正常 0: 锁定  -1：删除',
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=32)
    address = models.CharField(max_length=100)
    sex = models.CharField(max_length=4)


# 考生分组
class examineegroup(models.Model):
    groupid = models.CharField(max_length=32)
    userid = models.CharField(max_length=32)



#
# 试题库
class examlib(models.Model):
    examlib_id = models.CharField(max_length=32,primary_key=True)
    title = models.TextField()
    options = models.CharField(max_length=4000)
    anser = models.CharField(max_length=100)
    Type = models.CharField(max_length=50) #     '题目类型--单选single、多选multiple，判断judge',
    createtime=models.CharField(max_length=30)



#分组信息
class groupinfo(models.Model):
    groupinfo_id = models.CharField(max_length=32,primary_key=True)    
    groupname = models.CharField(max_length=255)
    createtime=models.CharField(max_length=30)



#考生考试记录
class records(models.Model):
      records_id = models.CharField(max_length=32,primary_key=True)  
      examid = models.CharField(max_length=32)  
      weigth = models.CharField(max_length=50)
      userid = models.CharField(max_length=30)  
      Type = models.CharField(max_length=50)
      sort = models.CharField(max_length=255)
      testid = models.CharField(max_length=32)
      title = models.TextField()
      options = models.CharField(max_length=4000)
      anser = models.CharField(max_length=100)
      myanser = models.CharField(max_length=100)
      score =  models.CharField(max_length=255)




#      
#考生考试记录
class records_copy(models.Model):
      records_copy_id = models.CharField(max_length=32,primary_key=True)  
      examid = models.CharField(max_length=32)  
      weigth = models.CharField(max_length=50)
      userid = models.CharField(max_length=30)  
      Type = models.CharField(max_length=50)
      sort = models.CharField(max_length=255)
      testid = models.CharField(max_length=32)
      title = models.TextField()
      options = models.CharField(max_length=4000)
      anser = models.CharField(max_length=100)
      myanser = models.CharField(max_length=100)
      score =  models.CharField(max_length=255)



    
#套题
class topics(models.Model):
      topics_id = models.CharField(max_length=32,primary_key=True)  
      name = models.CharField(max_length=255)
      singlenumber = models.CharField(max_length=50)
      singleweight = models.CharField(max_length=50)
      multiplenumber= models.CharField(max_length=50)
      multipleweight = models.CharField(max_length=50)
      judgenumber  = models.CharField(max_length=50)
      judgeweight =  models.CharField(max_length=50)
      tiankongnumber  = models.CharField(max_length=50)
      tiankongweight =  models.CharField(max_length=50)



#      考试总分
class totalscores(models.Model):
    totalscores_id = models.CharField(max_length=32) 
    examid = models.CharField(max_length=32) 
    userid = models.CharField(max_length=32) 
    score = models.CharField(max_length=50) 
    createtime = models.CharField(max_length=20) 
    status = models.CharField(max_length=20) # '状态 0 表示未考试 1表示已生成试卷',





