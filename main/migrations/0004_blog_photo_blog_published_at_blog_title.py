# Generated by Django 5.1.4 on 2025-05-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(default='ImgBlog/default.jpg', upload_to='ImgBlog'),
        ),
        migrations.AddField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Без названия', max_length=255),
        ),
    ]
