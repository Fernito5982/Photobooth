# Generated by Django 4.1.7 on 2023-04-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_usuarios_post_userimg_alter_perfil_profileimg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userImg',
            field=models.ImageField(default='bpp.webp', upload_to='profile_images'),
        ),
    ]
