# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from turtle import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PalpiteArquivo(models.Model):
    id_parq = models.AutoField(primary_key=True)
    palp_file = models.FileField(upload_to="files/%Y/%m/%d")
    palp_file_nome = models.CharField(max_length=100, blank=True, null=True)
    parq_dt_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.palp_file_nome)

class Palpite(models.Model):

    id_palp = models.AutoField(primary_key=True)
    palp_dt_criacao = models.DateTimeField(auto_now=True)
    palp_dezenas = models.CharField(max_length=100)
    palp_file = models.ForeignKey(PalpiteArquivo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_palp)
