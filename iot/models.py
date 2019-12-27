from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Device(models.Model):
    name = models.CharField(max_length=255,verbose_name="设备名称")
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name="设备编码")
    key = models.CharField(max_length=255,blank=True, null=True, verbose_name="设备秘钥")
    tags = models.CharField(max_length=255,blank=True, null=True, verbose_name="设备标签")
    about = models.TextField(blank=True, null=True, verbose_name="设备描述")
    locate = models.CharField(max_length=255,blank=True, null=True, verbose_name="设备位置")
    gps = models.CharField(max_length=255,blank=True, null=True, verbose_name="设备坐标")
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name="所属用户")
    create_time = models.DateTimeField(blank=True, null=True, verbose_name="创建时间")
    last_active = models.DateTimeField(blank=True, null=True, verbose_name="更新时间")
    status = models.IntegerField(choices=((0,0), (1,1)), default=1,verbose_name="设备状态")

    class Meta:
        verbose_name = "设备"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DeviceToken(models.Model):
    device = models.ForeignKey(Device, models.DO_NOTHING, verbose_name="设备")
    token = models.TextField(unique=True, verbose_name="临时口令")
    deadline = models.DateTimeField(verbose_name="有效时间")

    class Meta:
        verbose_name = "设备口令"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.token


class SensorType(models.Model):
    name = models.CharField(max_length=255,verbose_name="传感器类型")
    unit = models.CharField(max_length=255,blank=True, null=True,verbose_name="计量单位")
    desc = models.TextField(blank=True, null=True,verbose_name="类型备注")
    status = models.IntegerField(choices=((0,0), (1,1)),default=1,verbose_name="类型状态")

    class Meta:
        verbose_name = "传感器类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=255,verbose_name="传感器名称")
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name="传感器编码")
    type = models.ForeignKey(SensorType, models.DO_NOTHING,verbose_name="传感器类型")
    tags = models.TextField(blank=True, null=True,verbose_name="传感器标签")
    desc = models.TextField(blank=True, null=True,verbose_name="传感器描述")
    device = models.ForeignKey(Device, models.DO_NOTHING,verbose_name="所属设备")
    last_update = models.DateTimeField(blank=True, null=True,verbose_name="上次数据时间")
    last_data = models.TextField(blank=True, null=True,verbose_name="上次数据")
    status = models.IntegerField(choices=((0,0), (1,1)),default=1,verbose_name="传感器状态")

    class Meta:
        verbose_name = "传感器"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Datapoint(models.Model):
    sensor = models.ForeignKey(Sensor, models.DO_NOTHING,verbose_name="所属传感器")
    value = models.TextField(verbose_name="传感器数据")
    collect_time = models.TextField(blank=True, null=True,verbose_name="测量时间")
    report_time = models.DateTimeField(auto_now_add=True,verbose_name="上传时间")

    class Meta:
        verbose_name = "数据点"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value
