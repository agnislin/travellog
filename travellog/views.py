from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import User
# Create your views here.


def index(request):
    latest_question_list = User.objects.order_by('-id')
    template = loader.get_template('travellog/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
