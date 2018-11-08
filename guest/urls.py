from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from sign import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url("^$", views.login),
    url('^login_action/$', views.index),
    url('^login/$', views.login),
    url('index/logout/', views.logout, name="logout"),
    url('login_action/test/', views.test, name="test"),
    url('login_action/baidu/', views.baidu, name="baidu"),
    url('^accounts/login/$', views.login),
    url('login/register/$', views.register, name="regist"),
    url('^regist_action/$', views.regist_action),
    url('^api/',include(('sign.urls',"sign"),namespace="sign")),

]
