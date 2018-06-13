# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from performance.models import Performance
# from performance.serializers import PerformanceModelSerializer


def performance(request):
    return HttpResponse("hello world")


# class PerformanceRfView(APIView):
#     authentication_classes = ()
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         return Response("hello world")
#
#
# class PerformanceDbView(APIView):
#     authentication_classes = ()
#     permission_classes = (AllowAny,)
#     serializer_class = PerformanceModelSerializer
#
#     def post(self, request):
#         Performance.objects.create(name="testtesttesttesttesttesttesttest1",
#                                    phone="12345678901",
#                                    age=30,
#                                    gender='male',
#                                    address="shanghaishiputuoqujinshajiangxilu2145hao",
#                                    company="shanghaiqingkexinxijishuyouxiangongsi")
#
#         return Response("create ok")
#
#     def get(self, request):
#         p = Performance.objects.get(id=1)
#
#         return Response(self.serializer_class(instance=p).data)
