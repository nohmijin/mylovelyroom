from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'sex', 'contact', 'title', 'content', 'file', 'pet', 'bill', 'address2', 'file2']
        labels  = {
        'title':'방 제목', 
        'content':'방 소개', 
        'file':'방 이미지', 
        'pet':'애완동물여부', 
        'bill':'제시가격(월세)',
        'address2':'방 주소(위치)',
        'file2':'전대차 동의서',
        'name':'전대인 이름',
        'sex':'전대인 성별',
        'contact':'전대인 연락처'
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False
        self.fields['file2'].required = False