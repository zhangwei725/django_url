import datetime
import decimal
import json
from collections import Iterable

from django.http import HttpResponse, JsonResponse
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
from view01.models import TFilm, Girl


def index(request):
    return render(request, 'index.html')


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
    return render()


# post  请求的参数放在请求体
# get 请求的数据放在请求头里
#  请求头
#  请求行
#  请求体
# 一个get请求  一个post请求
def req_post(request):
    # 如果用户发送的请求方式是get请求
    if request.method == 'GET':
        return render(request, 'account/login.html')
    elif request.method == 'POST':
        # x-www-form-urlencoded
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse('登录成功')
    else:
        return HttpResponse('不支持的请求方式')


# jsonResponse
def movies(request):
    try:
        # 获取前10条数据
        films = TFilm.objects.all()[0:10]
        # 将QuerySet对象的数据转化列表套字典
        result = to_list(films)
        # films_json = json.dumps(result)
        data = {
            'status': 200,
            'msg': 'success',
            'data': result
        }
    except:
        # 错误的是返回的数据
        data = {'status': 404, 'msg': 'error'}
    return JsonResponse(data)


# 将对象转化成字典对象
def obj_to_dict(obj):
    result = {}
    if obj:
        # 将对象所有属性值,转化成字典形式
        keys = vars(obj).keys()
        if keys:
            for key in keys:
                if not key.startswith('_'):
                    value = getattr(obj, key)
                    if isinstance(value, datetime.datetime):
                        value = value.strftime('%Y-%m-%d %H:%i:%s ')
                    elif isinstance(value, datetime.date):
                        value = value.strftime('%Y-%m-%d')
                    elif isinstance(value, decimal.Decimal):
                        value = float(value)
                    result[key] = value
    return result


# 将QuerySet对象转化列表套字典
def to_list(objects):
    li = []
    if objects and isinstance(objects, Iterable):
        for obj in objects:
            li.append(obj_to_dict(obj))
    return li


import requests

"""
        "_id": "5be14edb9d21223dd50660f8",
        "createdAt": "2018-11-06T08:20:43.656Z",
        "desc": "2018-11-06",
        "publishedAt": "2018-11-06T00:00:00.0Z",
        "source": "web",
        "type": "福利",
        "url": "https://ws1.sinaimg.cn/large/0065oQSqgy1fwyf0wr8hhj30ie0nhq6p.jpg",
        "used": true,
        "who": "lijinshanmx"

"""


def load_data(request):
    response = requests.get('https://gank.io/api/data/%E7%A6%8F%E5%88%A9/600/1')
    fuli = json.loads(response.text)
    girls = []
    for obj in fuli['results']:
        girl = Girl()
        girl.type = obj.get('type')
        girl.source = obj.get('source')
        girl.desc = obj.get('desc')
        girl.created_date = obj.get('createdAt')
        girl.published = obj.get('publishedAt')
        girl.used = obj.get('used')
        girl.url = obj.get('url')
        girls.append(girl)
    Girl.objects.bulk_create(girls)
    return HttpResponse('so easy!!!!')
