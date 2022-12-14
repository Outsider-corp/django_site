# Generated by Django 4.1 on 2022-08-19 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_time', 'title'], 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=150, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Time'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo/%Y-%m-%d/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_publ',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]
