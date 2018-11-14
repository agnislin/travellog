from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Account
# Create your views here.

from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
import time
from .forms import PhotoForm
from .models import Photo


# def index(request):
#     latest_question_list = Account.objects.order_by('-id')
#
# # 模板的加载方式
#     # 1. 通过loader对象获取模板，再通过HttpResponse进行响应
#     template = loader.get_template('travellog/index.html')
#
#     #传递的数据类型(value)可以是: 字符串，整数，列表，元组，字典，函数，对象
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#
#     return HttpResponse(template.render(context, request)) # 接收context数据，将模板渲染并返回字符串
#     # 2. 使用render 直接加载并响应模板
#     # renturn render(request, template, context)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def visit(request):
    print(request.method)
    if request.method == "GET":
        return render(request, 'travellog/visit.html')

    name = request.POST.get("name", "匿名游客")
    code = request.POST.get("code", None)
    print(name, code)

    return render(request, 'travellog/index.html')


def uploadAlbum(request):
    print(request.method)
    if request.method == "GET":
        return render(request, 'travellog/uploadAlbum.html')






class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'travellog/userAdmin.html', {'photos': photos_list})

    def post(self, request):
        #time.sleep(3)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)



def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))
