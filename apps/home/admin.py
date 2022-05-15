# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin


from apps.home.models import PalpiteArquivo, Palpite

admin.site.register(PalpiteArquivo)
admin.site.register(Palpite)
