# Generated by Django 2.0 on 2018-01-14 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('pdid', models.IntegerField()),
                ('comment', models.CharField(max_length=200, verbose_name='评论内容')),
                ('commenttime', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('dailyid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('dailyname', models.CharField(max_length=20, verbose_name='日志名')),
                ('daily', models.TextField(verbose_name='日志内容')),
                ('postingdate', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('modifytime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerInfo',
            fields=[
                ('adminid', models.AutoField(primary_key=True, serialize=False)),
                ('adminname', models.CharField(max_length=20, verbose_name='管理员')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('tel', models.CharField(max_length=20, verbose_name='联系电话')),
                ('regtime', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageid', models.AutoField(primary_key=True, serialize=False)),
                ('blogid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('message', models.CharField(max_length=200, verbose_name='留言内容')),
                ('messagetime', models.DateTimeField(auto_now_add=True, verbose_name='留言时间')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('albumid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('albumname', models.CharField(max_length=30, verbose_name='相册名')),
                ('albumdepict', models.CharField(max_length=50, verbose_name='相册描述')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='建立时间')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoInfo',
            fields=[
                ('photoid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('albumid', models.IntegerField()),
                ('photoname', models.CharField(max_length=30, verbose_name='图片名')),
                ('photoaddress', models.CharField(max_length=50, verbose_name='图片地址')),
                ('photodepict', models.CharField(max_length=50, verbose_name='图片描述')),
                ('uploadtime', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('blogname', models.CharField(max_length=30, verbose_name='博客名')),
                ('blogsign', models.CharField(max_length=50, verbose_name='博客个性签名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('lastlogin', models.DateTimeField(auto_now=True, verbose_name='最后登录时间')),
                ('name', models.CharField(max_length=16)),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('province', models.CharField(max_length=20, verbose_name='省份')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('birthday', models.CharField(max_length=16, verbose_name='生日')),
                ('email', models.EmailField(max_length=30, verbose_name='邮箱')),
                ('tel', models.CharField(max_length=20, verbose_name='手机号')),
                ('regtime', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('profile', models.CharField(max_length=200, verbose_name='简介')),
                ('delflag', models.CharField(max_length=16)),
            ],
        ),
    ]
