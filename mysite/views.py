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
def bihua(request):
    course = request.GET.get('course')
    CourseHanziArray_D = []  # 課程生字
    #課程對應資料庫
    course_models={
          'Grade3F_L1': ThirdgradeF_LessonOneHanzi,
          'Grade3F_L2': ThirdgradeF_LessonTwoHanzi,
          'Grade3F_L3': ThirdgradeF_LessonThreeHanzi,
          'Grade3F_L4': ThirdgradeF_LessonFourHanzi,
          'Grade3F_L5': ThirdgradeF_LessonFiveHanzi,
          'Grade3F_L6': ThirdgradeF_LessonSixHanzi,
          'Grade3F_L7': ThirdgradeF_LessonSevenHanzi,
          'Grade3F_L8': ThirdgradeF_LessonEightHanzi,
          'Grade3F_L9': ThirdgradeF_LessonNineHanzi,
          'Grade3F_L10': ThirdgradeF_LessonTenHanzi,
          'Grade3F_L11': ThirdgradeF_LessonElevenHanzi,
          'Grade3F_L12': ThirdgradeF_LessonTwelveHanzi,

          'Grade3S_L1': ThirdgradeF_LessonOneHanzi,
          'Grade3S_L2': ThirdgradeF_LessonTwoHanzi,
          'Grade3S_L3': ThirdgradeF_LessonThreeHanzi,
          'Grade3S_L4': ThirdgradeF_LessonFourHanzi,
          'Grade3S_L5': ThirdgradeF_LessonFiveHanzi,
          'Grade3S_L6': ThirdgradeF_LessonSixHanzi,
          'Grade3S_L7': ThirdgradeF_LessonSevenHanzi,
          'Grade3S_L8': ThirdgradeF_LessonEightHanzi,
          'Grade3S_L9': ThirdgradeF_LessonNineHanzi,
          'Grade3S_L10': ThirdgradeF_LessonTenHanzi,
          'Grade3S_L11': ThirdgradeF_LessonElevenHanzi,
          'Grade3S_L12': ThirdgradeF_LessonTwelveHanzi,
    }
    if course in course_models:
     HanziCourse = course_models[course].objects.all().order_by('id')
     json_data = serializers.serialize('json', HanziCourse)

     
    else:
     CourseHanziArray_D = ['沒', '有', '抓', '到', '資', '料']
    CourseHanziArray_D = list(HanziCourse.values_list('Hanzi', flat=True)) #檢索 Hanzi 欄位的值，並將這些值以列表的形式返回

    return render(request, 'grade/type/bihua.html', locals())



