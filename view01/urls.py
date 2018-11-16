from django.conf.urls import url
from django.contrib import admin

from view01 import views
from view02 import views as v1

urlpatterns = [
    url('get/', views.req_get),
    url('post/', views.req_post),
    url('movies/', views.movies),
    url('load/', views.load_data),

]
