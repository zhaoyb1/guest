#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from sign import views_if

urlpatterns=[
    url('^add_event/',views_if.add_event,name="add_event"),
]
