from django.db import models

# Create your models here.
class test(models.Model):
    Hanzi = models.CharField(max_length=20,null=False)
    Radical = models.CharField(max_length=20,null=True)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateField(null=False)
    def __str__(self):
        return self.Radical
""" first semester上學期 F表示 跟second semester下學期表示S """
""" 三上第一課 """
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





