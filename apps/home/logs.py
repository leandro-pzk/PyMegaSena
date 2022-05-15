import json
import requests
from apps.home.models import Palpite, PalpiteArquivo


class GerarLogs:

    def logs_palpite_arquivo(request, p_arq):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            palpite_arquivo = PalpiteArquivo.objects.filter(id_parq=p_arq).values()
            for i in palpite_arquivo:
                i['ip'] = ip
                i['usuario'] = request.user.username

            data = json.dumps(list(palpite_arquivo), default=str)
            logs = requests.post('http://pymegasenalogs-master-web-1:8001/api/v1/logs/arquivo', json=data)
            print(logs)
        except:
            print(logs)

    
    def logs_palpite(request, palpite):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            palpite = Palpite.objects.filter(id_palp=palpite).values()
            for i in palpite:
                i['ip'] = ip
                i['usuario'] = request.user.username

            data = json.dumps(list(palpite), default=str)
            logs = requests.post('http://pymegasenalogs-master-web-1:8001/api/v1/logs/palpite', json=data)
        except:
            print('logs')
