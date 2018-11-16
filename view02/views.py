from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 基于的视图
from django.views import View
from django.views.decorators.csrf import csrf_exempt


def login(request):
    if request.method == 'GET':

        return ''
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


# get  post  put  delete   head


class LoginView(View):
    # get请求
    def get(self, request):
        print('1111')
        return render(request, 'account/login.html')

    # post请求
    @csrf_exempt
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse('登录')

    @csrf_exempt
    def put(self, request):
        print('222222')
        return HttpResponse('put')


# 动态路由案例
# ?page=10&size=20
# request

"""
第一步  在路由中使用正则表达式  
url(r'list/(\d+)/(\d+)/', v1.list),
第二歩 主要的作用用来传递参数 在视图函数中声明参数
def list(request, page):
第三分部  在浏览器中可以通过下面的方式来请求接口
/list/1/20/
# 注意事项
动态路径的正则的参数个数一定要跟视图函数的中参数一致
"""


def list(request, page, a):
    # return HttpResponse(f'当前第{page},{size}条')
    return HttpResponse('11111')


# 关键字动态路由
# 通过用户的id修改用户信息


# url(r'list/(?P<uid>\d+)/', v1.update),
# uid 视图函数动态参数必须跟路由定义的关键字一致

def update(request, uid):
    return HttpResponse(uid)
