from django.conf.urls import url
from django.contrib import admin

from view02 import views

urlpatterns = [
    url('login/', views.LoginView.as_view()),
    url(r'list/(\d+)/(\d+)/', views.list),
    url(r'update/(?P<uid>\d+)/', views.update),


]
