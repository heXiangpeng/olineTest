# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from models import examinee,examlib,groupinfo,exam,topics,examineegroup,totalscores,records
from json import loads,dumps
from datetime import datetime
from django.db.models import Q
import json
import sys
import string
import random
KEY_LEN = 20
reload(sys)
sys.setdefaultencoding( "utf-8" )


def base_str():
    return (string.letters+string.digits)

def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))


# Create your views here.
@csrf_exempt
def login(request):
    return render(request, 'login.html')


#添加考生
@csrf_exempt
def addorupdate(request):
    if request.POST:
        print request.body
        json_data = json.loads(request.body)
        for da in json_data:
            group = examineegroup()
            group.groupid = da['groupid']
            group.userid = da['userid']
            group.save()
        dic={}
        dic['staut']=0
        return HttpResponse(dumps(dic), content_type='application/json')
    else:
        dic={}
        dic['staut']=1
        return HttpResponse(dumps(dic), content_type='application/json')

#组织考试
@csrf_exempt
def examadd(request):
    if request.POST:
        print request.body
        da = json.loads(request.body)
        ex = exam()
        ex.exam_id = datetime.now().strftime('%Y%m%d%H%M%S')
        ex.examname = str(da['examname'])
        ex.begintime = da['begintime']
        ex.endtime = da['endtime']
        ex.groupid = da['groupid']
        ex.topicid = da['topicid']
        ex.save()
        grou = examineegroup.objects.filter(groupid__exact=da['groupid'])
        for gr in grou:
             print("group")
             totalscore = totalscores()
             totalscore.totalscores_id = datetime.now().strftime('%Y%m%d%H%M%S')+key_gen()
             totalscore.examid = ex.exam_id
             totalscore.userid = gr.userid
             totalscore.score="-1"
             totalscore.createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
             totalscore.status = "0"
             totalscore.save()
        dic={}
        dic['staut']=0
        return HttpResponse(dumps(dic), content_type='application/json')
    else:
        dic={}
        dic['staut']=1
        return HttpResponse(dumps(dic), content_type='application/json')

#管理界面
@csrf_exempt
def admin(request):
    return render(request, 'index_admin.html') 

#查询考生的信息
@csrf_exempt
def getbyuserid(request):
    if request.GET:
        userid = request.GET['userid']
        use = examinee.objects.filter(userid__exact=userid)
        if use:
            dic={}
            dic['staut']=0
            dic['userid'] = use[0].userid
            dic['username'] = use[0].username
            dic['ticketnumber'] = use[0].ticketnumber
            dic['idcard'] = use[0].idcard
            dic['actstatus'] = use[0].actstatus
            dic['phone'] = use[0].phone
            dic['email'] = use[0].email
            dic['address'] = use[0].address
            dic['sex'] = use[0].sex
            print dic
            return HttpResponse(dumps(dic), content_type='application/json')
        else:
            dic={}
            dic['staut']=1
            return HttpResponse(dumps(dic), content_type='application/json')

    else:
        dic={}
        dic['staut']=2
        return HttpResponse(dumps(dic), content_type='application/json')

                
#获取所有考试分组
@csrf_exempt
def examall(request):
     if request.GET:
         ex = exam.objects.all()
         objectdic = {}
         arr = []
         for us in ex:
            dic={}
            dic['staut']=0
            dic['id'] = us.exam_id
            dic['examname'] = us.examname
            dic['topicid'] = us.topicid
            group = groupinfo.objects.get(groupinfo_id=us.groupid)
            topic = topics.objects.get(topics_id=us.topicid)
            dic['groupname'] =  group.groupname
            dic['topicname'] =  topic.name
            dic['groupid'] = us.groupid
            dic['begintime'] = us.begintime
            dic['endtime'] = us.endtime
            arr.append(dic)
         objectdic["data"] = arr     
         return HttpResponse(dumps(objectdic), content_type='application/json')  


#判断题上传
@csrf_exempt
def judgechoice(request):
    return render(request, 'judge_choice.html') 

#套题设置
@csrf_exempt
def topicaddorupdate(request):
     if request.POST:
         topic = request.GET['topicid']
         judgenumber = request.POST['judgenumber']
         judgeweight = request.POST['judgeweight']
         multiplenumber = request.POST['multiplenumber']
         multipleweight = request.POST['multipleweight']
         name = request.POST['name']
         singlenumber = request.POST['singlenumber']
         singleweight = request.POST['singleweight']
         tiangkongnumber = request.POST['tiangkongnumber']
         tiangkongweight = request.POST['tiangkongweight']
         print topic
         if topic=='':

           exam =topics()
           exam.topics_id = datetime.now().strftime('%Y%m%d%H%M%S')
           exam.judgenumber = judgenumber
           exam.judgeweight = judgeweight
           exam.multiplenumber = multiplenumber
           exam.multipleweight = multipleweight
           exam.name = name
           exam.singlenumber = singlenumber
           exam.singleweight = singleweight
           exam.tiankongnumber = tiangkongnumber
           exam.tiankongweight = tiangkongweight
           exam.save()
           dic={}
           dic['staut']=0
           return HttpResponse(dumps(dic), content_type='application/json')
         else:
             exam = topics.objects.get(topics_id=topic)
             exam.judgenumber = judgenumber
             exam.judgeweight = judgeweight
             exam.multiplenumber = multiplenumber
             exam.multipleweight = multipleweight
             exam.name = name
             exam.singlenumber = singlenumber
             exam.singleweight = singleweight
             exam.tiankongnumber = tiangkongnumber
             exam.tiankongweight = tiangkongweight
             exam.save()
             dic = {}
             dic['staut'] = 0
             return HttpResponse(dumps(dic), content_type='application/json')


     else:
         dic={}
         dic['staut']=2
         return HttpResponse(dumps(dic), content_type='application/json')

#组织考试
@csrf_exempt
def group(request):
    if request.GET:
         ex = groupinfo.objects.all()
         objectdic = {}
         arr = []
         for us in ex:
            dic={}
            dic['staut']=0
            dic['id'] = us.groupinfo_id
            dic['groupname'] = us.groupname
            dic['createtime'] = us.createtime
            arr.append(dic)
         objectdic["data"] = arr     
         return HttpResponse(dumps(objectdic), content_type='application/json')

# 查看组的人数
@csrf_exempt
def groupexaminee(request):
    if request.GET:
        groupid =  request.GET['groupid']
        print(groupid)
        group = examineegroup.objects.filter(groupid__exact=groupid)
        arr = []
        objectdic = {}
        for us in group:
            print(us.userid)
            ex = examinee.objects.get(userid=us.userid)
            dic = {}
            dic['userid'] = ex.userid
            dic['username'] = ex.username
            dic['ticketnumber'] = ex.ticketnumber
            dic['idcard'] = ex.idcard
            dic['phone'] = ex.phone
            dic['actstatus'] = ex.actstatus
            arr.append(dic)
        objectdic["data"] = arr
        return HttpResponse(dumps(objectdic), content_type='application/json')

# 组添加人数
@csrf_exempt
def groupadduser(request):
    if request.GET:
        groupid =  request.GET['groupid']
        user = examinee.objects.all()
        objectdic = {}
        arr = []
        for us in user:
           group = examineegroup.objects.filter(groupid__exact=groupid,userid__exact=us.userid)
           dic = {}
           if group:
               print ("none")
           else:
              print("asjbjkbas")
              dic['staut'] = 0
              dic['userid'] = us.userid
              dic['username'] = us.username
              dic['ticketnumber'] = us.ticketnumber
              dic['idcard'] = us.idcard
              dic['actstatus'] = us.actstatus
              dic['phone'] = us.phone
              dic['email'] = us.email
              dic['address'] = us.address
              dic['sex'] = us.sex
              arr.append(dic)
        objectdic["data"] = arr
        return HttpResponse(dumps(objectdic), content_type='application/json')


#删除组
@csrf_exempt
def deleteuseringroup(request):
    if request.GET:
        userid = request.GET['userid']
        obj = examineegroup.objects.get(userid=userid)
        obj.delete()
        dic = {}
        dic['staut'] = 0
        return HttpResponse(dumps(dic), content_type='application/json')





    #组织考试
@csrf_exempt
def topicgetAll(request):
      if request.GET:
         ex = topics.objects.all()
         objectdic = {}
         arr = []
         for us in ex:
            dic={}
            dic['staut']=0
            dic['id'] = us.topics_id
            dic['name'] = us.name
            dic['singlenumber'] = us.singlenumber
            dic['singleweight'] = us.singleweight
            dic['multiplenumber'] = us.multiplenumber
            dic['multipleweight'] = us.multipleweight
            dic['judgenumber'] = us.judgenumber
            dic['judgeweight'] = us.judgeweight
            dic['tiankongnumber'] = us.tiankongnumber
            dic['tiankongweight'] = us.tiankongweight
            arr.append(dic)
         objectdic["data"] = arr     
         return HttpResponse(dumps(objectdic), content_type='application/json')  


#组织考试
def groupall(request):
     if request.GET:
         ex = groupinfo.objects.all()
         objectdic = {}
         arr = []
         for us in ex:
            dic={}
            dic['staut']=0
            dic['id'] = us.groupinfo_id
            dic['groupname'] = us.groupname
            dic['createtime'] = us.createtime
            arr.append(dic)
         objectdic["data"] = arr     
         return HttpResponse(dumps(objectdic), content_type='application/json')  


#组织考试
@csrf_exempt
def organizationexam(request):
    return render(request, 'organization_exam.html')


#编辑考试
@csrf_exempt
def editexam(request):
    if request.GET:
        examid = request.GET['examid']
        exa = exam.objects.get(exam_id=examid)
        dic = {}
        dic['id'] = exa.exam_id
        dic['examname'] = exa.examname
        dic['groupid'] = exa.groupid
        dic['topicid'] = exa.topicid
        group = groupinfo.objects.get(groupinfo_id=exa.groupid)
        dic['groupname'] = group.groupname
        top = topics.objects.get(topics_id=exa.topicid)
        dic['topicname'] = top.name
        dic['begintime'] = exa.begintime
        dic['endtime'] = exa.endtime
        return HttpResponse(dumps(dic), content_type='application/json')


# 删除考试
@csrf_exempt
def deleteexam(request):
    if request.GET:
        examid = request.GET['examid']
        exa = exam.objects.get(exam_id=examid)
        exa.delete()
        dic = {}
        dic['staut'] = 0
        return HttpResponse(dumps(dic), content_type='application/json')


#用户添加
@csrf_exempt
def examineeadd(request):
    if request.POST:
         userid = request.GET['userid']
         username = request.POST['username']
         ticketnumber = request.POST['ticketnumber']
         idcard = request.POST['idcard']
         password = request.POST['password']
         actstatus  = request.POST['actstatus']
         phone = request.POST['phone']
         email = request.POST['email']
         address = request.POST['address']
         sex = request.POST['sex']
         print(userid)
         if userid != '':
            exam = examinee.objects.get(userid=userid)
            exam.username = username
            exam.ticketnumber = ticketnumber
            exam.idcard = idcard
            exam.password = password
            exam.actstatus = actstatus
            exam.phone = phone
            exam.email = email
            exam.address = address
            exam.sex = sex
            print
            exam
            exam.save()
            dic={}
            dic['staut']=0
            return HttpResponse(dumps(dic), content_type='application/json')
         else:  
            exam = examinee()
            exam.userid = datetime.now().strftime('%Y%m%d%H%M%S')
            exam.username = username
            exam.ticketnumber = ticketnumber
            exam.idcard = idcard
            exam.password = password
            exam.actstatus = actstatus
            exam.phone = phone
            exam.email = email
            exam.address = address
            exam.sex = sex
            print exam
            exam.save()
            dic={}
            dic['staut']=0
            return HttpResponse(dumps(dic), content_type='application/json')

    else:
          dic={}
          dic['staut']=2
          return HttpResponse(dumps(dic), content_type='application/json')





 #获取所有的用户
@csrf_exempt
def getAll(request):
       user = examinee.objects.all()
       objectdic = {}
       arr = []
       for us in user:
            dic={}
            dic['staut']=0
            dic['userid'] = us.userid
            dic['username'] = us.username
            dic['ticketnumber'] = us.ticketnumber
            dic['idcard'] = us.idcard
            dic['actstatus'] = us.actstatus
            dic['phone'] = us.phone
            dic['email'] = us.email
            dic['address'] = us.address
            dic['sex'] = us.sex
            arr.append(dic)
       objectdic["data"] = arr     
       return HttpResponse(dumps(objectdic), content_type='application/json')    




@csrf_exempt      
def examineecount(request):
    uer =  examinee.objects.all()
    cout  =  len(uer)
    dic={}
    dic["rc"] = 0
    dic["data"] = cout
    return HttpResponse(dumps(dic), content_type='application/json')



@csrf_exempt
def examineestudent(request):
    return render(request, 'examinee.html')



 #    查看题目
@csrf_exempt
def examlibview(request):
    if request.GET:
        id = request.GET['id']
        exam = examlib.objects.get(examlib_id=id)
        dic = {}
        dic['staut'] = 0
        dic['id'] = exam.examlib_id
        dic['title'] = exam.title
        dic['options'] = exam.options
        dic['answer'] = exam.anser
        return HttpResponse(dumps(dic), content_type='application/json')

 #    删除题目
@csrf_exempt
def examlibvdelete(request):
    if request.GET:
        id = request.GET['id']
        exam = examlib.objects.get(examlib_id=id)
        exam.delete()
        dic = {}
        dic['staut'] = 0
        return HttpResponse(dumps(dic), content_type='application/json')

#获取题目
@csrf_exempt
def examlibtypesingle(request):
    if request.GET:
        Tpe = request.GET['typle']
        exam = examlib.objects.filter(Type__exact=Tpe)
        objectdic = {}
        arr = []
        for us in exam:
          dic={}
          dic['staut']=0
          dic['id'] = us.examlib_id
          dic['title'] = us.title
          dic['options'] = us.options
          dic['answer'] = us.anser
          arr.append(dic)
        objectdic["data"] = arr     
        return HttpResponse(dumps(objectdic), content_type='application/json')  

 #考生分批
def examineebatch(request):
    return render(request, 'examinee_batch.html') 


 #单选题
@csrf_exempt
def singlechoice(request):
    return render(request, 'single_choice.html') 

@csrf_exempt
def multiplechoice(request):    
    return render(request, 'multiple_choice.html')



#添加填空
@csrf_exempt
def tiankongadd(request):
     if request.POST:
         title = request.POST['title']
         answer = request.POST['answer']
         Type = request.POST['Type']
         exam =examlib()
         exam.examlib_id = datetime.now().strftime('%Y%m%d%H%M%S')
         exam.title = title
         exam.options = ""
         exam.anser = answer
         exam.Type = Type
         exam.createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         exam.save()
         dic={}
         dic['staut']=0
         return HttpResponse(dumps(dic), content_type='application/json')

     else:
         dic={}
         dic['staut']=2
         return HttpResponse(dumps(dic), content_type='application/json')





#添加题目
@csrf_exempt
def examlibadd(request):
     if request.POST:
         title = request.POST['title']
         options = request.POST['options']
         answer = request.POST['answer']
         Type = request.POST['Type']
         exam =examlib()
         exam.examlib_id = datetime.now().strftime('%Y%m%d%H%M%S')
         exam.title = title
         exam.options = options
         exam.anser = answer
         exam.Type = Type
         exam.createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         exam.save()
         dic={}
         dic['staut']=0
         return HttpResponse(dumps(dic), content_type='application/json')

     else:
         dic={}
         dic['staut']=2
         return HttpResponse(dumps(dic), content_type='application/json')


 
#添加分组
@csrf_exempt
def groupaddorupdate(request):
    if request.POST:
         groupname = request.POST['groupname']
         group = groupinfo()
         group.groupname = groupname
         group.groupinfo_id = datetime.now().strftime('%Y%m%d%H%M%S')
         group.createtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         group.save()
         dic={}
         dic['staut']=0
         return HttpResponse(dumps(dic), content_type='application/json')



 #管理套题
@csrf_exempt
def maketest(request):
    return render(request, 'make_test.html')


 #编辑套题
@csrf_exempt
def editmaketest(request):
    if request.GET:
        topicid = request.GET['topicid']
        exam = topics.objects.get(topics_id=topicid)
        dic = {}
        dic['staut'] = 0
        dic['id'] = exam.topics_id
        dic['name'] = exam.name
        dic['singlenumber'] = exam.singlenumber
        dic['singleweight'] = exam.singleweight
        dic['multiplenumber'] = exam.multiplenumber
        dic['multipleweight'] = exam.multipleweight
        dic['judgenumber'] = exam.judgenumber
        dic['judgeweight'] = exam.judgeweight
        dic['tiankongnumber'] = exam.tiankongnumber
        dic['tiankongweight'] = exam.tiankongweight
        return HttpResponse(dumps(dic), content_type='application/json')



@csrf_exempt
def userlogin(request):
     if request.POST:
         username = request.POST['idcard']
         psw = request.POST['psw']
         use = examinee.objects.filter(phone__exact=username,password__exact=psw)
         if use:
             dic={}
             dic['staut']=0
             dic['userid'] = use[0].userid
             dic['username'] = use[0].username
             dic['ticketnumber'] = use[0].ticketnumber
             dic['idcard'] = use[0].idcard
             dic['actstatus'] = use[0].actstatus
             dic['phone'] = use[0].phone
             dic['email'] = use[0].email
             dic['address'] = use[0].address
             dic['sex'] = use[0].sex
             request.session['userid'] = use[0].userid

             print dic
             return HttpResponse(dumps(dic), content_type='application/json')
         else:
             dic={}
             dic['staut']=1
             return HttpResponse(dumps(dic), content_type='application/json')

# 添加分组
@csrf_exempt
def updateexam(request):
    if request.POST:
        da = json.loads(request.body)
        userid = request.session.get('userid', default='')
        print(userid)
        obj = examinee.objects.get(userid=userid)
        obj.address = da['address']
        obj.email = da['email']
        print(obj.address)
        obj.password = da['newpassword']
        obj.username = da['username']
        print(obj.password)
        obj.save()
        dic = {}
        dic['staut'] = 0
        return HttpResponse(dumps(dic), content_type='application/json')
    else:
        dic = {}
        dic['staut'] = 1
        return HttpResponse(dumps(dic), content_type='application/json')

# 删除
@csrf_exempt
def groupdelete(request):
    if request.GET:
        groupid = request.GET['groupid']
        examineegroup.objects.filter(groupid=groupid).delete()
        groupinfo.objects.filter(groupinfo_id=groupid).delete()
        dic = {}
        dic['staut'] = 0
        return HttpResponse(dumps(dic), content_type='application/json')






 #学生端主页
@csrf_exempt
def indexstdudent(request):
    return render(request, 'index_examinee.html') 


 #学生端主页
@csrf_exempt
def lineexam(request):
     return render(request, 'online_exam.html')


     

#学生考试
@csrf_exempt
def scoresuserid(request):
      if request.GET:
        userid = request.GET['userid']
        total = totalscores.objects.filter(userid__exact=userid)
        objectdic = {}
        arr = []
        for ex in total:
            dic={}

            re = records.objects.filter(examid__exact=ex.examid)
            if re:
                dic['staut'] = 1
            else:
                dic['staut']=0
            exa = exam.objects.get(exam_id=ex.examid)
            dic['examname'] = exa.examname
            dic['examid'] = exa.exam_id
            dic['begintime'] = exa.begintime
            dic['endtime'] = exa.endtime
            arr.append(dic)
        objectdic['data'] = arr    
        return HttpResponse(dumps(objectdic), content_type='application/json')    


@csrf_exempt
def openexam(request):
    if request.GET:
        examid = request.GET['examid']
        return render(request, 'openexam.html')

    # 个人成绩查询
@csrf_exempt
def scorepersonal(request):
    return render(request, 'score_personal.html')

#个人成绩查询
@csrf_exempt
def analyticsexam(request):
    return render(request, 'analytics_exam.html')


@csrf_exempt
def tiangkong(request):
    return render(request, 'tiankong.html')


#个人成绩查询
@csrf_exempt
def navbar(request):
        return render(request, 'navbar.html')

#个人成绩查询
@csrf_exempt
def mysetting(request):
        return render(request,'mysetting.html')


@csrf_exempt
def recordshistory(request):
    if request.GET:
        examid = request.GET['examid']
        ex = exam.objects.filter(exam_id__exact=examid)[0]
        topic = topics.objects.filter(topics_id__exact=ex.topicid)[0]
        siglenumber = topic.singlenumber
        # 获取单选题目个数
        objec = {}
        userid = request.session.get('userid', default='')
        record = records.objects.filter(examid__exact=examid, userid__exact=userid,Type__exact="single")
        sigleindex = 0
        arrsigle=[]
        for ex in record:
                dic = {}
                sigleindex += 1
                dic['sort'] = sigleindex
                dic['id'] = ex.testid
                dic['title'] = ex.title
                dic['options'] = ex.options
                dic['answer'] = ex.anser
                dic['myanser'] = ex.myanser
                dic['weight'] = ex.weigth
                arrsigle.append(dic)

        record = records.objects.filter(examid__exact=examid, userid__exact=userid, Type__exact="multiple")
        arrmut = []
        sigleindex = 0

        for ex in record:
            dic = {}
            sigleindex += 1
            dic['sort'] = sigleindex
            dic['id'] = ex.testid
            dic['title'] = ex.title
            dic['options'] = ex.options
            dic['answer'] = ex.anser
            dic['myanser'] = ex.myanser
            dic['weight'] = ex.weigth
            print(ex.myanser)
            arrmut.append(dic)

        record = records.objects.filter(examid__exact=examid, userid__exact=userid, Type__exact="judge")
        arrjude = []
        sigleindex = 0

        for ex in record:
            dic = {}
            sigleindex += 1
            dic['sort'] = sigleindex
            dic['answer'] = ex.anser
            dic['id'] = ex.testid
            dic['title'] = ex.title
            dic['options'] = ex.options
            dic['myanser'] = ex.myanser
            dic['weight'] = ex.weigth
            arrjude.append(dic)

        record = records.objects.filter(examid__exact=examid, userid__exact=userid, Type__exact="tiankong")
        arrtiankong = []
        sigleindex = 0

        for ex in record:
            dic = {}
            sigleindex += 1
            dic['sort'] = sigleindex
            dic['answer'] = ex.anser
            dic['id'] = ex.testid
            dic['title'] = ex.title
            dic['options'] = ex.options
            dic['myanser'] = ex.myanser
            dic['weight'] = ex.weigth
            arrtiankong.append(dic)

        objectdic = {}
        objectdic['single'] = arrsigle
        objectdic['multiple'] = arrmut
        objectdic['judge'] = arrjude
        objectdic['tiangkong'] = arrtiankong
        objec['data'] = objectdic
        objec['rc'] = 0
        return HttpResponse(dumps(objec), content_type='application/json')

# 计算成绩
@csrf_exempt
def score(request):
    if request.GET:
        userid = request.GET['userid']
        recor = records.objects.filter(userid__exact=userid)
        print userid
        us = examinee.objects.filter(userid__exact=userid)[0]
        #先取出做了多少份试卷
        arrexam = []
        index = 1
        for re in recor:
            if index == 1:
                arrexam.append(re.examid)

            index += 1
            iscontain = 1
            for arr in arrexam:
                if arr == re.examid:
                    iscontain = 2
            if iscontain == 1:
                arrexam.append(re.examid)
            iscontain=1
         #计算所有套题的分数
        arr = []
        for exa in arrexam:
             score = 0
             for re in recor:
                 if exa == re.examid:
                     score += int(re.score)

             ex = exam.objects.get(exam_id=exa)
             dic={}
             dic['score'] = score
             dic['examname'] = ex.examname
             dic['username'] = us.username
             dic['idcard'] = us.idcard
             arr.append(dic)
        objectdic = {}
        objectdic['data'] = arr
        return HttpResponse(dumps(objectdic), content_type='application/json')

# 系统管理员查看人员的分数
@csrf_exempt
def admimlookscore(request):
    if request.GET:
        examid = request.GET['examid']
        recor=records.objects.filter(examid__exact=examid)
        ex = exam.objects.filter(exam_id__exact=examid)[0]
        #获取所有的用户
        arruser = []
        index = 1
        for re in recor:
            if index == 1:
                arruser.append(re.userid)

            index += 1
            iscontain = 1
            for arr in arruser:
                if arr == re.userid:
                    iscontain = 2
            if iscontain == 1:
                arruser.append(re.userid)
            iscontain = 1


            # 计算所有用户的分数
        arr = []
        for use in arruser:
            for re in recor:
                score = 0
                if use==re.userid:
                    score += int(re.score)
            user = examinee.objects.filter(userid__exact=use)[0]
            dic = {}
            dic['score'] = score
            dic['examname'] = ex.examname
            dic['username'] = user.username
            dic['idcard'] = user.idcard
            arr.append(dic)

        objectdic = {}
        objectdic['rc'] = 0
        objectdic['data'] = arr
        return HttpResponse(dumps(objectdic), content_type='application/json')




    #完成试卷初始化
@csrf_exempt     
def recordsinit(request):
    if request.GET:
        examid = request.GET['examid']
        ex = exam.objects.filter(exam_id__exact=examid)[0]
        topic = topics.objects.filter(topics_id__exact=ex.topicid)[0]
        siglenumber = topic.singlenumber
        print siglenumber
        #获取单选题目个数
        userid = request.session.get('userid',default='')
        obj = getcacherecorde(examid,userid,topic)
        if obj!="":
           dic = getcacherecorde(examid,userid,topic)
           objec = {}
           objec['data'] = dic
           objec['rc'] = 0
           return HttpResponse(dumps(objec), content_type='application/json')
        else:
           dic = initrecords(examid,userid,topic)
           objec = {}
           objec['data'] = dic
           objec['rc'] = 0
           return HttpResponse(dumps(objec), content_type='application/json')

# 上传试卷
@csrf_exempt
def uploadanser(request):
    if request.POST:
        examid = request.GET['eximid']
        print examid
        da = json.loads(request.body)
        for x in da:
          obj = records.objects.get(Q(testid=x['id']),Q(examid=examid))
          obj.myanser = x['myanswer']
          print x['myanswer']
          if obj.anser == x['myanswer']:
              obj.score = obj.weigth
          obj.save()
          print "save"
        objec = {}
        objec['rc'] = 0
        return HttpResponse(dumps(objec), content_type='application/json')


        #初始化题库
def initrecords(examid,userid,topic):
        examsigle = examlib.objects.filter(Type__exact="single")
        print len(examsigle)
        objectdic = {}
        arrsigle = []
        sigleindex = 0
        sigle = random_int_list(0,len(examsigle)-1,topic.singlenumber)
        print sigle
        for ex in sigle:
             dic={}
             sigleindex += 1
             dic['sort'] = sigleindex
             dic['id'] = examsigle[ex].examlib_id
             dic['title'] = examsigle[ex].title
             dic['options'] = examsigle[ex].options
             dic['weight'] = topic.singleweight
             arrsigle.append(dic)
             #将题目存储到考生考试记录里面
             record = records()
             record.records_id = datetime.now().strftime('%Y%m%d%H%M%S')+key_gen()
             record.examid = examid
             record.weigth = topic.singleweight
             record.userid = userid
             record.Type = "single"
             record.sort = sigleindex
             record.testid = examsigle[ex].examlib_id
             record.title = examsigle[ex].title
             record.options = examsigle[ex].options
             record.anser = examsigle[ex].anser
             record.myanser = ""
             record.score = "0"
             record.save()

        exammut = examlib.objects.filter(Type__exact="multiple")
        arrmut = []
        sigleindex = 0
        sigle = random_int_list(0,len(exammut)-1,topic.multiplenumber)
        for ex in sigle:
             dic={}
             sigleindex += 1
             dic['sort'] = sigleindex
             dic['id'] = exammut[ex].examlib_id
             dic['title'] = exammut[ex].title
             dic['options'] = exammut[ex].options
             dic['weight'] = topic.multipleweight
             arrmut.append(dic)
              #将题目存储到考生考试记录里面
             record = records()
             record.records_id = datetime.now().strftime('%Y%m%d%H%M%S')+key_gen()
             record.examid = examid
             record.weigth = topic.multipleweight
             record.userid = userid
             record.Type = "multiple"
             record.sort = sigleindex
             record.testid = exammut[ex].examlib_id
             record.title = exammut[ex].title
             record.options = exammut[ex].options
             record.anser = exammut[ex].anser
             record.myanser = ""
             record.score = "0"
             record.save()   

        exajudge = examlib.objects.filter(Type__exact="judge")
        arrjude = []
        sigleindex = 0
        sigle = random_int_list(0,len(exajudge)-1,topic.judgenumber)
        print sigle
        for ex in sigle:
             dic={}
             sigleindex += 1
             dic['id'] = exajudge[ex].examlib_id
             dic['sort'] = sigleindex
             dic['title'] = exajudge[ex].title
             dic['options'] = exajudge[ex].options
             dic['weight'] = topic.judgeweight
             arrjude.append(dic)
              #将题目存储到考生考试记录里面
             record = records()
             record.records_id = datetime.now().strftime('%Y%m%d%H%M%S')+key_gen()
             record.examid = examid
             record.weigth = topic.judgeweight
             record.userid = userid
             record.Type = "judge"
             record.sort = sigleindex
             record.testid = exajudge[ex].examlib_id
             record.title = exajudge[ex].title
             record.options = exajudge[ex].options
             record.anser = exajudge[ex].anser
             record.myanser = ""
             record.score = "0"
             record.save()

        exatiankong = examlib.objects.filter(Type__exact="tiankong")
        arrtiankong = []
        sigleindex = 0
        sigle = random_int_list(0, len(exatiankong) - 1, topic.tiankongnumber)
        for ex in sigle:
            dic = {}
            print("填空")
            sigleindex += 1
            dic['id'] = exatiankong[ex].examlib_id
            dic['sort'] = sigleindex
            dic['title'] = exatiankong[ex].title
            dic['options'] = exatiankong[ex].options
            dic['weight'] = topic.tiankongweight
            arrtiankong.append(dic)
            # 将题目存储到考生考试记录里面
            record = records()
            record.records_id = datetime.now().strftime('%Y%m%d%H%M%S') + key_gen()
            record.examid = examid
            record.weigth = topic.tiankongweight
            record.userid = userid
            record.Type = "tiankong"
            record.sort = sigleindex
            record.testid = exatiankong[ex].examlib_id
            record.title = exatiankong[ex].title
            record.options = exatiankong[ex].options
            record.anser = exatiankong[ex].anser
            record.myanser = ""
            record.score = "0"
            record.save()

        objectdic['single'] = arrsigle
        objectdic['multiple'] = arrmut
        objectdic['judge'] = arrjude
        objectdic['tiangkong'] = arrtiankong
        return objectdic     


#获取缓存的试卷
def getcacherecorde(examid,userid,topic):
    record = records.objects.filter(examid__exact=examid,userid__exact=userid)
    if record:
          #获取单选题目个数
        examsigle = examlib.objects.filter(Type__exact="single")
        print len(examsigle)
        objectdic = {}
        arrsigle = []
        sigleindex = 0
        for ex in examsigle:
             dic={}
             sigleindex += 1
             dic['sort'] = sigleindex
             dic['id'] = ex.examlib_id
             dic['title'] = ex.title
             dic['options'] = ex.options
             dic['anser'] = ex.myanser
             arrsigle.append(dic)

        exammut = examlib.objects.filter(Type__exact="multiple")
        arrmut = []
        sigleindex = 0
     
        for ex in exammut:
             dic={}
             sigleindex += 1
             dic['sort'] = sigleindex
             dic['id'] = ex.examlib_id
             dic['title'] = ex.title
             dic['options'] = ex.options
             dic['anser'] = ex.myanser
             arrmut.append(dic)
            
        exajudge = examlib.objects.filter(Type__exact="judge")
        arrjude = []
        sigleindex = 0

        for ex in exajudge:
             dic={}
             sigleindex += 1
             dic['sort'] = sigleindex
             dic['anser'] = ex.myanser
             dic['id'] = ex.examlib_id
             dic['title'] = ex.title
             dic['options'] = ex.options
             arrjude.append(dic)

             exatiangkong = examlib.objects.filter(Type__exact="tiankong")
             arrtiangkong = []
             sigleindex = 0

             for ex in exatiangkong:
                 dic = {}
                 sigleindex += 1
                 dic['sort'] = sigleindex
                 dic['anser'] = ex.myanser
                 dic['id'] = ex.examlib_id
                 dic['title'] = ex.title
                 dic['options'] = ex.options
                 arrtiangkong.append(dic)



        objectdic['single'] = arrsigle
        objectdic['multiple'] = arrmut
        objectdic['judge'] = arrjude
        objectdic['tiangkong'] = arrtiangkong


        return objectdic
        
    else:
        return ""






#生成随机数组
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(length) if length else 0
    random_list = []
    for i in range(start, length):
        random_list.append(i)
    return random_list








    #     use = examinee()
    # use.userid="56f2db42c57469433dff08bc"
    # use.username = "化缘"
    # use.ticketnumber="1459049619668"
    # use.password = "1234560"
    # use.actstatus = "1"
    # use.phone = "18314462409"
    # use.email = "1483767097@qq.com"
    # use.address ="云南丽江"
    # use.sex = "1"
    # use.save()     