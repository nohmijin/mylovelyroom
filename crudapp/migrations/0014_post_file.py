# Generated by Django 2.2.1 on 2019-05-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0013_remove_post_file1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]