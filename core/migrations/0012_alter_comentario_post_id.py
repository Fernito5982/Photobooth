# Generated by Django 4.1.7 on 2023-05-16 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_comentario_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.post'),
        ),
    ]
