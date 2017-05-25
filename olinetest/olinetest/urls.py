"""olinetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from exame import views as appview

urlpatterns = [
    url('admin',  appview.admin),
    url(r'^login', appview.login),
    url(r'^userlogin', appview.userlogin),
    url(r'^examinee/count', appview.examineecount),
    url(r'^examineestudent', appview.examineestudent),
    url(r'^examinee/getAll', appview.getAll),
    url(r'^examinee/get', appview.getbyuserid),
    url(r'^examinee/add', appview.examineeadd),
    url(r'^examinee/maketest', appview.maketest),
    url(r'^examinee/singlechoice', appview.singlechoice),
    url(r'^examinee/examlibadd', appview.examlibadd),
    url(r'^examinee/examlib/type/single', appview.examlibtypesingle),
    url(r'^multiplechoice', appview.multiplechoice),
    url(r'^examineebatch', appview.examineebatch),
    url(r'^group/addorupdate', appview.groupaddorupdate),
    url(r'^organizationexa', appview.organizationexam),
    url(r'^exam/all', appview.examall),
    url(r'^examinee/topic/getAll', appview.topicgetAll),
    url(r'^judgechoice', appview.judgechoice),
    url(r'^topicaddorupdate', appview.topicaddorupdate),
    url(r'^group', appview.group),
    url(r'^examineegroup/addorupdate', appview.addorupdate),
    url(r'^exam/addorupdate', appview.examadd),
    url(r'^indexexaminee', appview.indexstdudent),
    url(r'^onlineexam', appview.lineexam),
    url(r'^scores/userid', appview.scoresuserid),
    url(r'^open', appview.openexam),
    url(r'^records/init', appview.recordsinit),
    url(r'^uploadanser', appview.uploadanser),
    url(r'^records/history', appview.recordshistory),
    url(r'^scorepersonal', appview.scorepersonal),
    url(r'^mysetting', appview.mysetting),
    url(r'^navbar', appview.navbar),
    url(r'^score', appview.score),
    url(r'^analyticsexam', appview.analyticsexam),
    url('lookscores', appview.admimlookscore),
    url('examinee/update/examinee', appview.updateexam),
    url('tiangkong', appview.tiangkong),
    url('examinee/tiankongadd', appview.tiankongadd),
    url('examlib/id', appview.examlibview),
    url('examlib/delete', appview.examlibvdelete),
    url('examinee/topic/get', appview.editmaketest),
    url('examineegroup/get', appview.groupexaminee),
    url('examineegroup/delete', appview.deleteuseringroup),
    url('exam/id', appview.editexam),
    url('exam/delete', appview.deleteexam),
    url('deletegroup', appview.groupdelete),
    url('AllByActStatus', appview.groupadduser),




]
