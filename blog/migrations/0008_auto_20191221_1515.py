# Generated by Django 2.2 on 2019-12-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]
