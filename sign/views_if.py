#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import JsonResponse


def add_event(request):
    eid = request.POST.get("eid")
    name = request.POST.get("name")
    limit = request.POST.get("limit")
    status = request.POST.get("status")

    if eid == "" or name == "" or limit == '' or status == "":

        return JsonResponse({"status": 10001, "message": "参数不能为空"})

    if eid=="1" and name=="zhangsan" and limit=="2" and status=="1":

        return JsonResponse({"status": 200, "message": "success"})

    else:

        print(eid,name,limit,status)
        print(type(eid))

        return JsonResponse({"status":10002,"message":"value error"})
