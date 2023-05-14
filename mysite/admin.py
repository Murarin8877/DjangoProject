

from django.contrib import admin
from mysite import models
""" from mysite.models import test,LessonOneHanzi """

# Register your models here.
class testAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Radical','cSex','cBirthday' ]
    list_filter=('cSex',)
    search_fields=('Hanzi',) 
admin.site.register(models.test,testAdmin)
""" first semester上學期 F表示 跟second semester下學期表示S """
""" 三上第一課 """
class ThirdgradeF_LessonOneHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonOneHanzi,ThirdgradeF_LessonOneHanziAdmin)

class ThirdgradeF_LessonTwoHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonTwoHanzi,ThirdgradeF_LessonTwoHanziAdmin)

class ThirdgradeF_LessonThreeHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonThreeHanzi,ThirdgradeF_LessonThreeHanziAdmin)

class ThirdgradeF_LessonFourHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonFourHanzi,ThirdgradeF_LessonFourHanziAdmin)

""" 三上第五課 """
class ThirdgradeF_LessonFiveHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonFiveHanzi,ThirdgradeF_LessonFiveHanziAdmin)

class ThirdgradeF_LessonSixHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonSixHanzi,ThirdgradeF_LessonSixHanziAdmin)

class ThirdgradeF_LessonSevenHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']   
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonSevenHanzi,ThirdgradeF_LessonSevenHanziAdmin)

class ThirdgradeF_LessonEightHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonEightHanzi,ThirdgradeF_LessonEightHanziAdmin)

class ThirdgradeF_LessonNineHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonNineHanzi,ThirdgradeF_LessonNineHanziAdmin)

""" 三上第十課 """
class ThirdgradeF_LessonTenHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonTenHanzi,ThirdgradeF_LessonTenHanziAdmin)


class ThirdgradeF_LessonElevenHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonElevenHanzi,ThirdgradeF_LessonElevenHanziAdmin)

class ThirdgradeF_LessonTwelveHanziAdmin(admin.ModelAdmin):
    list_display = ['id','Hanzi','Bopomofo','Radical','R_Bopomofo','Total_strokes']    
    search_fields=('Hanzi',) 
admin.site.register(models.ThirdgradeF_LessonTwelveHanzi,ThirdgradeF_LessonTwelveHanziAdmin)
