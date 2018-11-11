# Generated by Django 2.1.2 on 2018-11-06 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='收件地址')),
                ('name', models.CharField(max_length=20, verbose_name='收件人')),
                ('mobile', models.CharField(max_length=30, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '用户地址',
                'verbose_name_plural': '用户地址',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('head_img', models.ImageField(blank=True, default='', max_length=500, upload_to='static/user/%Y/%m', verbose_name='头像')),
                ('mobile', models.CharField(max_length=11, verbose_name='联系方式')),
                ('wechat', models.CharField(max_length=100, verbose_name='微信')),
                ('integral', models.IntegerField(default=0, verbose_name='积分')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='余额')),
                ('open_id', models.CharField(max_length=100, verbose_name='OpenId')),
                ('remark', models.TextField(verbose_name='备注')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
            },
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile', verbose_name='用户'),
        ),
    ]
