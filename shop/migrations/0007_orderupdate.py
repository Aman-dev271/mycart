# Generated by Django 2.2.7 on 2019-11-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.ImageField(default='', upload_to='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('itemstamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
