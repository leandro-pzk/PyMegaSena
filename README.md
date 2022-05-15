# PyMegaSena

Instruções para execução do sistema:

1. Realizar o donwload dos arquivos deste diretório
2. Tem a instalação mais recente do docker desktop
3. docker-compose build
4. docker-compose up
5. Caso o banco de dados não tenha sido compilado em tempo de execução, realizar:
6. docker-compose down e apos conclusão, docker-compose up
7. Em outro terminal executar: docker-compose exec web sh
8. python manage.py createsuperuser
9. python manage.py migrate
10. Abrir a aplicação em localhost:8000
