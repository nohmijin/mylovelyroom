# Generated by Django 2.2.1 on 2019-05-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0016_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='agreement',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]