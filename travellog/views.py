from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User
# Create your views here.


def index(request):
    latest_question_list = User.objects.order_by('-id')

# 模板的加载方式
    # 1. 通过loader对象获取模板，再通过HttpResponse进行响应
    template = loader.get_template('travellog/index.html')

    #传递的数据类型(value)可以是: 字符串，整数，列表，元组，字典，函数，对象
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request)) # 接收context数据，将模板渲染并返回字符串
    # 2. 使用render 直接加载并响应模板
    # renturn render(request, template, context)
