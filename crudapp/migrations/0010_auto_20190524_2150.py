# Generated by Django 2.2.1 on 2019-05-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0009_auto_20190524_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='file',
            new_name='file1',
        ),
        migrations.AlterField(
            model_name='post',
            name='address2',
            field=models.CharField(default='예) 서울시 강북구 수유동', max_length=50),
        ),
    ]