from django.conf.urls import url, include
from django.contrib import admin

from view01 import views

'''

'''

# 第一步在app中建一个url.py文件
# 第二歩 在根urls.py文件中 引入 app中路由 使用include函数
# 第三步,在app的urls.py文件中注册视图函数或者视图类
# 注意
# 在浏览器中访问的时候一定要加上一级路由中的路径

urlpatterns = [
    url('admin/', admin.site.urls),
    # 访问根域名默认的显示界面
    url('^$', views.index),
    # 2.0以上的写法
    # path('', views.index),
    url('view01/', include('view01.urls')),
    url('view02/', include('view02.urls')),
]
