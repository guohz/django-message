from django.shortcuts import render
from django.contrib import messages

def show_msg(request):
    add_msg(request)
    return render(request,'show_msg.html',{})


def add_msg(request):
    messages.add_message(request, messages.INFO, 'Hello world.')
    messages.debug(request, '调试消息')
    messages.info(request, '一般消息')
    messages.success(request, '成功消息')
    messages.warning(request, '警告消息')
    messages.error(request, '错误消息')
