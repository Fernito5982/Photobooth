# Generated by Django 4.1.7 on 2023-04-26 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_post_userimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='userImg',
        ),
    ]