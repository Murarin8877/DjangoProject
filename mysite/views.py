from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import *
from django.core import serializers #json 套件
# Create your views here.
def Hellow(request):
     return HttpResponse("Hello World!")


def index(request):
     return render(request,"index.html")
def login(request):
     return render(request,"login.html")

def grade(request):
     return render(request,"grade/grade.html")
def type(request):

     return render(request,"grade/type/type.html")

def keyboard(request):
     return render(request,"grade/type/keyboard.html")
def bihua(request,Semester,Lesson):
    dHanziCourse = Thirdgrade_CourseHanzi.objects.filter(cSemester=Semester,cLesson=Lesson)#取得cSemester,cLesson條件的資料列
    dHanziCourseArray = [hanzi.Hanzi for hanzi in dHanziCourse] #取得漢字陣列
    json_data = serializers.serialize('json', dHanziCourse)#取得其他欄位
    return render(request, 'grade/type/bihua.html', locals())



