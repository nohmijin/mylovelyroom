# Generated by Django 2.2.1 on 2019-05-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0015_remove_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]
