from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse,HttpResponseRedirect
from iot.models import Datapoint
import json
from django.views.decorators.csrf import csrf_exempt
from iot.forms import DatapointForm


def Index(request):
    return HttpResponseRedirect('/admin')


class HelpView(View):
    def get(self, request):
        return  render(request,"help.html")


def addhelp(request):
    dataform=DatapointForm()
    return render(request, "addhelp.html",{'dataform':dataform})


@csrf_exempt
def post_datapoint(request):
    """
     api/post_datapoint/   获得上传的post数据
    :param request:
    :return:
    """
    if request.method=="POST":
        print(request.POST["sensor"])
        item = request.POST
        data=Datapoint(sensor_id=int(item["sensor"]), value=item["value"], collect_time=item['collect_time'], )
        data.save()
        return HttpResponse("POST数据添加成功！")


@csrf_exempt
def json_datapoint(request):
    """
     api/json_datapoint/   获得上传的json数据
    :param request:
    :return:
    """
    if request.method=="POST":
        # print(request.body)
        request_data=json.loads(request.body)
        # 权限检查，检查head
        if not request_data:
            return HttpResponse("没有数据！")
        if not issubclass(dict, type(request_data)):
            return HttpResponse("数据必须为字典格式！")
        # print(request_data)
        datapoint_list = []
        for item in request_data["datapoints"]:
            # print(item["sensor"])
            datapoint_list.append(
                Datapoint(sensor_id=int(item["sensor"]),value=item["value"],collect_time=item['collect_time'], )
            )
        Datapoint.objects.bulk_create(datapoint_list)
        return HttpResponse("JSON数据添加成功！")
