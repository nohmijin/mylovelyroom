# Generated by Django 2.2.1 on 2019-05-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_auto_20190515_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='address1',
            field=models.IntegerField(choices=[('강남구', '강남구'), ('강동구', '강동구'), ('강북구', '강북구'), ('강서구', '강서구'), ('관악구', '관악구'), ('광진구', '광진구'), ('구로구', '구로구'), ('금천구', '금천구'), ('노원구', '노원구'), ('도봉구', '도봉구'), ('동대문구', '동대문구'), ('동작구', '동작구'), ('마포구', '마포구'), ('서대문구', '서대문구'), ('서초구', '서초구'), ('성동구', '성동구'), ('성북구', '성북구'), ('송파구', '송파구'), ('양천구', '양천구'), ('영등포구', '영등포구'), ('용산구', '용산구'), ('은평구', '은평구'), ('종로구', '종로구'), ('중구', '중구'), ('중랑구', '중랑구')], default=0),
        ),
    ]
