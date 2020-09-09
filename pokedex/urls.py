# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:42:03 2020

@author: ashva
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result', views.result, name="result")
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
