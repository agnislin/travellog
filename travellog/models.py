from django.db import models

# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length=32, unique=True, verbose_name="用户名") # Each field is represented by an instance of a Field class, like CharField
    password = models.CharField(max_length=128, verbose_name="")
    is_active = models.BooleanField(default=True)
    register_date = models.DateField(auto_now=True, null=True, verbose_name="注册时间")

    def __str__(self):
        return "%s: username: %s, active: ".format(self.__class__.name, username, is_active)


class Personal(models.Model):
    name = models.CharField(max_length=32, null=True, verbose_name="昵称")
    contact_way = models.CharField(max_length=32, null=True, verbose_name="联系方式")
    introduction = models.CharField(max_length=512, null=True, verbose_name="介绍")
    avatar = models.CharField(max_length=255, verbose_name="头像")
    tags = models.CharField(max_length=64, verbose_name="个性标签")

    def __str__(self):
        return "%s: name: %s".format(self.__class__.name, name)

class Picture(models.Model):
    picture_name = models.CharField(max_length=255, null=True, verbose_name="图片名")
    path = models.CharField(max_length=255, verbose_name="路径")
    album_group = models.ForeignKey(Album, related_name="pictures", verbose_name="所属相册")

    def __str__(self):
        return "%s: name: %s".format(self.__class__.name, picture_name)

class Album(models.Model):
    album_name = models.CharField(max_length=255, verbose_name="相册名")
    create_date = models.DateField(auto_now=True, verbose_name="创建时间")
    alter_time = models.DateField(auto_now=True, null=True, verbose_name="变更时间")
    description = models.CharField(max_length=512, null=True, verbose_name="描述")
    cover = models.CharField(max_length=255, null=True, verbose_name="封面路径")
    package = models.ForeignKey(Package, related_name="albums", verbose_name="所属包")

    def __str__(self):
        return "%s: name: %s".format(self.__class__.name, album_name)

class Package(models.Model):
    package_name = models.CharField(max_length=32, verbose_name="包名")
    create_date = models.DateField(auto_now=True, verbose_name="创建时间")
    title = models.CharField(max_length=64, null=True, verbose_name="描述标题")
    cover = models.CharField(max_length=255, null=True, verbose_name="封面路径")
    private = models.BooleanField(default=False, verbose_name="私人可见")
    author =

    def __str__(self):
        return "%s: name: %s".format(self.__class__.name, package_name)
# The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. You’ll use this value in your Python code, and your database will use it as the column name.
