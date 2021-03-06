# Generated by Django 2.1.3 on 2018-11-15 03:45

from django.db import migrations, models
import django.db.models.deletion
import travellog.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('is_active', models.BooleanField(default=True)),
                ('register_date', models.DateField(auto_now=True, null=True, verbose_name='注册时间')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=255, verbose_name='相册名')),
                ('create_date', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('alter_time', models.DateField(auto_now=True, null=True, verbose_name='变更时间')),
                ('description', models.CharField(max_length=512, null=True, verbose_name='描述')),
                ('cover', models.CharField(max_length=255, null=True, verbose_name='封面路径')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=32, verbose_name='包名')),
                ('create_date', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('title', models.CharField(max_length=64, null=True, verbose_name='描述标题')),
                ('cover', models.CharField(max_length=255, null=True, verbose_name='封面路径')),
                ('private', models.BooleanField(default=False, verbose_name='私人可见')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='packages', to='travellog.Account', verbose_name='所有者')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='昵称')),
                ('contact_way', models.CharField(max_length=32, null=True, verbose_name='联系方式')),
                ('introduction', models.CharField(max_length=512, null=True, verbose_name='介绍')),
                ('avatar', models.CharField(max_length=255, verbose_name='头像')),
                ('tags', models.CharField(max_length=64, verbose_name='个性标签')),
                ('personal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='travellog.Account', verbose_name='所属账号')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_name', models.CharField(max_length=255, null=True, verbose_name='图片名')),
                ('path', models.FileField(max_length=255, upload_to=travellog.models.user_directory_path, verbose_name='路径')),
                ('upload_time', models.DateField(auto_now=True, null=True, verbose_name='上传时间')),
                ('album_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='travellog.Album', verbose_name='所属相册')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='package',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='travellog.Package', verbose_name='所属包'),
        ),
    ]
