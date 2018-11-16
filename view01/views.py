from django.http import HttpResponse
from django.shortcuts import render

# 声明视图函数必须把request作为第一个参数
# request是由系统创建(不要手动去实例化request)
# GET属性
# POST属性
# PUT   DELETE   HEAD
# method  判断请求方式
# COOKIE
# session
# FILES
from view01.models import TFilm


def req(request):
    # request.GET
    # request.POST
    # request.method
    # request.COOKIES
    # request.session
    # request.FILES
    # request.path 获取当前的请求路径
    # request.META
    return HttpResponse()


# sort 排序字段  1表示降序  默认是升序
# http://127.0.0.1/get/?page=8&size=10&sort=1
# ?key=value&key=value
# request.GET 返回的类字典对象
# [start:end:step] 切片操作
# 多选  checkbox
def req_get(request):
    # get方法会的
    # request.GET.getlist()
    page = int(request.GET.get('page', 1))
    size = int(request.GET.get('size', 10))
    sort = request.GET.get('sort', 0)
    start = (page - 1) * size
    end = page * size
    # films = TFilm.objects.all()[start:end]
    qs = TFilm.objects.all().order_by('-update_time') if sort else TFilm.objects.all()
    # 先判断排序的参数
    # if sort:
    #     # 降序
    #     qs = qs.order_by('-update_time')
    films = qs[start:end]

    for film in films:
        print(film.name)
    return HttpResponse()


# post  请求的参数放在请求体
# get 请求的数据放在请求头里
#  请求头
#  请求行
#  请求体
# 一个get请求  一个post请求
def req_post(request):
    # 如果用户发送的请求方式是get请求
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # x-www-form-urlencoded
        request.POST.get('username')
        request.POST.get('password')
        return HttpResponse('登录成功')
    else:
        return HttpResponse('不支持的请求方式')
