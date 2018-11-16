from django.contrib import admin
from django.urls import path

from view01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', views.req_get),
    path('post/', views.req_post),
]
