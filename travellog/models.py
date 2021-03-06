from django.db import models
import time

# Create your models here.
class Account(models.Model):
    user_name = models.CharField(max_length=32, unique=True, verbose_name="用户名") # Each field is represented by an instance of a Field class, like CharField
    password = models.CharField(max_length=128, verbose_name="密码")
    is_active = models.BooleanField(default=True)
    register_date = models.DateField(auto_now=True, null=True, verbose_name="注册时间")
    def __str__(self):
        return "{}: username: {}, active: ".format(self.__class__.__name__, self.user_name, self.is_active)


class Personal(models.Model):
    name = models.CharField(max_length=32, null=True, verbose_name="昵称")
    contact_way = models.CharField(max_length=32, null=True, verbose_name="联系方式")
    introduction = models.CharField(max_length=512, null=True, verbose_name="介绍")
    avatar = models.CharField(max_length=255, verbose_name="头像")
    tags = models.CharField(max_length=64, verbose_name="个性标签")
    personal = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="所属账号")

    def __str__(self):
        return "{}: name: {}".format(self.__class__.__name__, self.name)

class Package(models.Model):
    package_name = models.CharField(max_length=32, verbose_name="包名")
    create_date = models.DateField(auto_now=True, verbose_name="创建时间")
    title = models.CharField(max_length=64, null=True, verbose_name="描述标题")
    cover = models.CharField(max_length=255, null=True, verbose_name="封面路径")
    private = models.BooleanField(default=False, verbose_name="私人可见")
    author = models.ForeignKey(Account, related_name="packages", blank=True, null=True, on_delete=models.SET_NULL, verbose_name="所有者")

    def __str__(self):
        return "{}: name: {}".format(self.__class__.__name__, self.package_name)

class Album(models.Model):
    album_name = models.CharField(max_length=255, verbose_name="相册名")
    create_date = models.DateField(auto_now=True, verbose_name="创建时间")
    alter_time = models.DateField(auto_now=True, null=True, verbose_name="变更时间")
    description = models.CharField(max_length=512, null=True, verbose_name="描述")
    cover = models.CharField(max_length=255, null=True, verbose_name="封面路径")
    package = models.ForeignKey(Package, related_name="albums", blank=True, on_delete=models.CASCADE, verbose_name="所属包")

    def __str__(self):
        return "{}: name: {}".format(self.__class__.__name__, self.album_name)


def get_base_user_file_dir():
    return "/".join(["FileDB/", time.strftime("%Y/%m",time.localtime())])

def user_directory_path(instance, filename):
    base = get_base_user_file_dir()
    name = instance.picture_name
    album = instance.album_group.album_name
    pack = instance.album_group.package.package_name
    try:
        user = instance.album_group.package.author.user_name
    except AttributeError:
        user = "LOSS_USER"
    print([base, user, pack, album, name])
    return "/".join([base, user, pack, album, name])


class Picture(models.Model):
    picture_name = models.CharField(max_length=255, null=True, verbose_name="图片名")
    file = models.FileField(max_length=255, verbose_name="路径", upload_to=user_directory_path)
    album_group = models.ForeignKey(Album, related_name="pictures", on_delete=models.CASCADE, verbose_name="所属相册")
    upload_time = models.DateField(auto_now=True, null=True, verbose_name="上传时间")

    def __str__(self):
        return "{}: name: {}".format(self.__class__.__name__, self.picture_name)





def note():
    return """
            Field Types
                BooleanField() Boolean -> 0/1 tinyint
                CharField()    str -> varchar
                DateField()    str/date -> date
                DateTimeField() datetime
                DecimalField() decimal, money=models.DecimalField(max_digits=7,decimal_places=2)
                FloatField()
                IntegerField()
                EmailField()  str -> varchar
                URLField()    str -> varchar
                ImageField() varchar, image = models.ImageField(upload_to='images/users/')

            Field Options
                default, null, primary_key, db_column

            on_delete
                CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
                PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
                SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
                SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
                SET(): 自定义一个值，该值当然只能是对应的实体了

                a. 与之关联的值设置为指定值,设置：models.SET(值)
                b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
             """
