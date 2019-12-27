from django.http import HttpResponse,JsonResponse
from iot.models import Datapoint, Sensor
from _datetime import datetime
from django.shortcuts import render
import datetime as dt
import json


def searchdata(id, name):
    value_list = []
    time_list = []
    time_list1 = []
    main_dic = {}
    data = Datapoint.objects.all()
    for var in data:
        if var.sensor_id == id:
            value_list.append(var.value)
            time_list.append(var.collect_time)

    index = len(time_list)
    time1 = datetime.strptime(time_list[-1].split(".")[0], "%Y-%m-%d %H:%M:%S")
    time2 = dt.datetime(time1.year, time1.month, time1.day-1, time1.hour, time1.minute, time1.second,
                        time1.microsecond)
    for x in range(0, index):
        time3 = datetime.strptime(time_list[0].split(".")[0], "%Y-%m-%d %H:%M:%S")
        if time3 < time2:
            time_list.pop(0)
            value_list.pop(0)

    for n in time_list:
        n1=n.split(".")[0]
        n2=n1.split(" ")[1]
        time4 = datetime.strptime(n2, "%H:%M:%S")
        time5 = time4.strftime("%H:%M:%S")
        time_list1.append(time5)

    main_dic[name + "_value"] = value_list
    main_dic[name + "_time"] = time_list1
    return main_dic

def humidityjson(request):
    hd_dic = searchdata(9, "humidity01")
    hd_dic.update(searchdata(14, "humidity02"))
    return JsonResponse(hd_dic,json_dumps_params={'ensure_ascii':False},safe=False)

def humidity(request):
    return render(request, "humidity.html")

def temperaturejson(request):
    tp_dic = searchdata(10, "temperature01")
    tp_dic.update(searchdata(13, "temperature02"))
    return JsonResponse(tp_dic,json_dumps_params={'ensure_ascii':False},safe=False)

def temperature(request):
    return render(request, "temperature.html")

def searchAll(request):
    time_list = []
    name_list=[]
    main_dic = {}
    final_list=[]
    data = Datapoint.objects.all()
    sensor = Sensor.objects.all()
    for id in range(4, 13):
        for sor in sensor:
            if sor.id == id:
                name_list.append(sor.name)
    for var in data:
        if var.sensor_id == 4:
            time_list.append(var.collect_time)

    for i in range(0,len(time_list)):
        for var1 in data:
            if var1.collect_time==time_list[i]:
                s_id=int(var1.sensor_id)-4
                value=var1.value
                name=name_list[s_id].split("-")[0]
                main_dic[name]=value

        main_dic["测量时间"]=time_list[i]
        final_list.append(main_dic)
        main_dic={}

    # jsonData1 = json.dumps(final_list)
    # fileObject = open("test1.json", 'w',encoding="utf-8")
    # fileObject.write(jsonData1)
    # fileObject.close()

    return render(request,"datalist.html",{"rows":json.dumps(final_list)})
    # return HttpResponse("数据录入成功"+str(len(final_list)))

