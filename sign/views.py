# coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from sign.script import insert,select


# Create your views here.
def login(request):
    return render(request, "login.html")


def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 数据库的处理:判断用户
        if not select.select_user(username,password):

            return render(request, "login.html", {"error": "username or password error!"})
        else:

            res = render(request, "index.html", {"user": username})

            res.set_cookie('user', username)

            return res


    else:
        return render(request, "temp.html")


@login_required
def logout(request):
    return render(request, "login.html")


def test(request):

    userinfo=select.select_event()
    print(userinfo)
    return render(request, 'test.html',{"userinfo":userinfo})


def baidu(request):
    return render(request, 'baidu.html')


def index(request):
    return login_action(request)


def register(request):
    return render(request, 'register.html')


def regist_action(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 数据库的处理:入库
        insert.insert_userinfo(username,password)

        return render(request, "login.html")

    else:
        return render(request, "temp.html")
