# Generated by Django 2.1.7 on 2019-02-25 15:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scenicspots', '0002_gallery'),
        ('diarys', '0001_initial'),
        ('shop', '0001_initial'),
        ('operation', '0002_diarycomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('active', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenicspots.Active', verbose_name='活动')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '活动评论',
                'verbose_name_plural': '活动评论',
            },
        ),
        migrations.CreateModel(
            name='ProductComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=25, verbose_name='订单号')),
                ('comments', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='下单用户')),
            ],
            options={
                'verbose_name': '商品评论',
                'verbose_name_plural': '商品评论',
            },
        ),
        migrations.CreateModel(
            name='UserCollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏时间')),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diarys.Diary', verbose_name='游记')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '游记收藏',
                'verbose_name_plural': '游记收藏',
            },
        ),
    ]