# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models import Model


class Performance(Model):
    name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15)
    age = models.SmallIntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

