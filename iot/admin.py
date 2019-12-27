from django.contrib import admin
from .models import DeviceToken,Device,SensorType,Sensor,Datapoint

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display=('id','name','code', 'tags', 'about', 'locate', 'user', 'create_time', 'last_active', 'status', )

@admin.register(DeviceToken)
class DeviceTokenAdmin(admin.ModelAdmin):
    list_display=('id','device', 'token', 'deadline', )

@admin.register(SensorType)
class SensorTypeAdmin(admin.ModelAdmin):
    list_display=('id','name', 'desc', 'status', )

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display=('id','name','code', 'type', 'tags', 'desc', 'device', 'last_update', 'last_data', 'status', )

@admin.register(Datapoint)
class DatapointAdmin(admin.ModelAdmin):
    list_display=('id','sensor', 'value', 'collect_time', 'report_time', )
    list_filter = ('sensor', 'collect_time', 'report_time', )

admin.site.site_header = '物联网数据平台'

admin.site.site_title = '物联网数据平台'
