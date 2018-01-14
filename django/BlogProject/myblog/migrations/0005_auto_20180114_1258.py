# Generated by Django 2.0 on 2018-01-14 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20180114_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('adminid', models.AutoField(primary_key=True, serialize=False)),
                ('adminname', models.CharField(max_length=20, verbose_name='管理员')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='姓名')),
                ('tel', models.CharField(max_length=20, null=True, verbose_name='联系电话')),
                ('regtime', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
        ),
        migrations.DeleteModel(
            name='ManagerInfo',
        ),
        migrations.AddField(
            model_name='comment',
            name='nickname',
            field=models.CharField(max_length=50, null=True, verbose_name='昵称'),
        ),
        migrations.AddField(
            model_name='daily',
            name='keyword',
            field=models.CharField(max_length=20, null=True, verbose_name='关键字'),
        ),
        migrations.AddField(
            model_name='daily',
            name='tab',
            field=models.CharField(max_length=20, null=True, verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='message',
            name='messagename',
            field=models.CharField(max_length=50, null=True, verbose_name='留言姓名'),
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='keyword',
            field=models.CharField(max_length=20, null=True, verbose_name='关键字'),
        ),
        migrations.AddField(
            model_name='photoinfo',
            name='keyword',
            field=models.CharField(max_length=20, null=True, verbose_name='关键字'),
        ),
        migrations.AlterField(
            model_name='daily',
            name='modifytime',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='albumdepict',
            field=models.CharField(max_length=50, null=True, verbose_name='相册描述'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birthday',
            field=models.CharField(max_length=16, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='blogsign',
            field=models.CharField(max_length=50, null=True, verbose_name='博客个性签名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='city',
            field=models.CharField(max_length=20, null=True, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='delflag',
            field=models.IntegerField(choices=[(0, '普通用户'), (1, '高级用户')], default=1, verbose_name='用户类型标记'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=30, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile',
            field=models.CharField(max_length=200, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='province',
            field=models.CharField(max_length=20, null=True, verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.CharField(max_length=20, null=True, verbose_name='手机号'),
        ),
    ]