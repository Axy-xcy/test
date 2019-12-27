"""IotRestfulHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iot.views import HelpView
from iot import views,drawing

urlpatterns = [
    path('admin/help/', HelpView.as_view()),
    path('admin/addhelp/', views.addhelp, name="addhelp"),
    path('admin/', admin.site.urls),
    path('api/post_datapoint/', views.post_datapoint,name="post_datapoint"),
    path('api/json_datapoint/', views.json_datapoint, name="json_datapoint"),
    path('humidityjson/', drawing.humidityjson),
    path('admin/humidity/',drawing.humidity),
    path('temperaturejson/', drawing.temperaturejson),
    path('admin/temperature/',drawing.temperature),
    path('admin/datalist/',drawing.searchAll),
    path('',views.Index),
]
