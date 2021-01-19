# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:07:29 2021

@author: KANTY
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]