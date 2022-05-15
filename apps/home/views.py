# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json
import os
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
import pandas as pd
import requests
from django.core import serializers

from apps.home.forms import PalpiteArquivoForm
from apps.home.logs import GerarLogs
from apps.home.models import Palpite


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    if request.method == 'GET':
        api_mega_sena = requests.get('https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/')
        resultado = api_mega_sena.json()
        context['mega'] = resultado

    elif request.method == 'POST':
        concurso = request.POST.get('concurso')
        api_mega_sena = requests.get('https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/'+ concurso)
                                    
        if api_mega_sena.status_code == 200:
            resultado = api_mega_sena.json()
            context['mega'] = resultado

    html_template = loader.get_template('home/index.html')

    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def palpite(request):

    if request.method == 'POST':

        form_parq = PalpiteArquivoForm(request.POST, request.FILES)

        if (form_parq.is_valid()):
            form = form_parq.save()
            form.palp_file_nome = request.FILES['palp_file'].name
            form.save()

            GerarLogs.logs_palpite_arquivo(request, form.pk) # Gerar logs de insert 

        
        if str(form.palp_file_nome).endswith('.csv'):

            """
            Tratamento para arquivos .CSV
            """    
            df = pd.read_csv(form.palp_file.path)
            df = df.iloc[0].values.tolist()

            numeros = ','.join(str(e) for e in df)
            novo_palpite = Palpite(palp_dezenas=numeros.replace(';', ','), palp_file=form)
            novo_palpite.save()

            GerarLogs.logs_palpite(request, novo_palpite.pk) # Gerar logs

            return redirect(request.META['HTTP_REFERER'])

        elif str(form.palp_file_nome).endswith('.xlsx'):
            """
            Tratamento para arquivos .xlsx
            """
            df1 = pd.read_excel(form.palp_file.path, engine='openpyxl')
            df1 = df1.iloc[0].values.tolist()
    
            numeros = ','.join(str(e) for e in df1)

            novo_palpite = Palpite(palp_dezenas=numeros, palp_file=form)
            novo_palpite.save()

            GerarLogs.logs_palpite(request, novo_palpite.pk) # Gerar logs

            return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="/login/")
def administrar(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/administrar.html')

    palpites = Palpite.objects.all()
    serialized_obj = serializers.serialize('json', palpites)
  
    context['data'] = serialized_obj


    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
