from django.db import models

# Create your models here.
class Post(models.Model):

    name = models.CharField(max_length=15, default="실명")
    sex = models.CharField(max_length=10, default="여성 or 남성")
    contact = models.CharField(max_length=30, default="핸드폰번호")
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/') 
    bill = models.IntegerField(default=0)
    pet = models.BooleanField(default=True)
    address2 = models.CharField(max_length=50, default="예) 서울시 강북구 수유동")
    agreement = models.ImageField(upload_to='images/') 

    created_at = models.DateTimeField(auto_now_add=True) #만든시간
    updated_at = models.DateTimeField(auto_now=True) #수정시간

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:10]