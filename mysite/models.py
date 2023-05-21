from django.db import models

# Create your models here.
class test(models.Model):
    Hanzi = models.CharField(max_length=20,null=False)
    Radical = models.CharField(max_length=20,null=True)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateField(null=False)
    def __str__(self):
        return self.Radical


class Thirdgrade_CourseHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    cGrade = models.CharField(max_length=10,blank=False)
    cSemester = models.CharField(max_length=10,blank=False)
    cLesson = models.CharField(max_length=20,blank=False)
    def __str__(self):
        return self.Hanzi
""" first semester上學期 F表示 跟second semester下學期表示S """
""" 筆順練習三上第一課 """
class ThirdgradeF_LessonOneHanzi(models.Model): 
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
class ThirdgradeF_LessonTwoHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi 
class ThirdgradeF_LessonThreeHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
class ThirdgradeF_LessonFourHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
""" 三上第五課 """
class ThirdgradeF_LessonFiveHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
class ThirdgradeF_LessonSixHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi 
class ThirdgradeF_LessonSevenHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi 
class ThirdgradeF_LessonEightHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi 
class ThirdgradeF_LessonNineHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
""" 三上第十課 """
class ThirdgradeF_LessonTenHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi  
class ThirdgradeF_LessonElevenHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
""" 三上第十二課 """  
class ThirdgradeF_LessonTwelveHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi  


""" 筆順練習三下第一課 second semester下學期表示S """
class ThirdgradeS_LessonOneHanzi(models.Model): 
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
class ThirdgradeS_LessonTwoHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi 
class ThirdgradeS_LessonThreeHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
class ThirdgradeS_LessonFourHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
""" 三下第五課 """
class ThirdgradeS_LessonFiveHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
class ThirdgradeS_LessonSixHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi 
class ThirdgradeS_LessonSevenHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi 
class ThirdgradeS_LessonEightHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi 
class ThirdgradeS_LessonNineHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
""" 三下第十課 """
class ThirdgradeS_LessonTenHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi  
class ThirdgradeS_LessonElevenHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi
""" 三下第十二課 """  
class ThirdgradeS_LessonTwelveHanzi(models.Model):
    Hanzi = models.CharField(max_length=1,null=False)
    Bopomofo = models.CharField(max_length=25,null=False)
    Radical = models.CharField(max_length=1,null=True,blank=True)
    R_Bopomofo= models.CharField(max_length=10,null=True,blank=True)    
    Total_strokes = models.IntegerField(null=False)
    def __str__(self):
        return self.Hanzi  



