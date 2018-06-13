# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.serializers import ModelSerializer

from performance.models import Performance


class PerformanceModelSerializer(ModelSerializer):

    class Meta:
        model = Performance
