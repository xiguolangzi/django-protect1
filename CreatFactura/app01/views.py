from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("欢迎使用！！")



def user_list(request):
    # 返回页面 render
    #默认去app 下 找对应的 templates目录中找 (回去所有注册的app中去寻找，按顺序查找)
    #具体查找目录，优先找配置文件settings 中 TEMPLATES ，dir 寻找
    return render(request,"user_list.html")


def user_add(request):
    return  HttpResponse("添加用户")