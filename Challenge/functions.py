import json

import geocoder
import requests


def siglaEstado(estado):
    switch = {
        'Acre': 'AC',
        'Alagoas': 'AL',
        'Amapá': 'AP',
        'Amazonas': 'AM',
        'Bahia': 'BA',
        'Ceará': 'CE',
        'Distrito Federal': 'DF',
        'Espírito Santo': 'ES',
        'Goiás': 'GO',
        'Maranhão': 'MA',
        'Mato Grosso': 'MT',
        'Mato Grosso do Sul': 'MS',
        'Minas Gerais': 'MG',
        'Pará': 'PA',
        'Paraíba': 'PB',
        'Paraná': 'PR',
        'Pernambuco': 'PE',
        'Piauí': 'PI',
        'Rio de Janeiro': 'RJ',
        'Rio Grande do Norte': 'RN',
        'Rio Grande do Sul': 'RS',
        'Rondônia': 'RO',
        'Roraima': 'RR',
        'Santa Catarina': 'SC',
        'São Paulo': 'SP',
        'Sergipe': 'SE',
        'Tocantins': 'TO'
    }
    return switch.get(estado)


def getLocation():
    g = geocoder.ip('me')
    return siglaEstado(g.state)


def empresa():
    request = requests.get(f"https://app-challenge-api.herokuapp.com/plans?state={'MG'}")
    todo = json.loads(request.content)
    lista = []
    for i in range(0, len(todo)):
        lista.insert(1,f"Preço: {todo[i]['id']}  ISP: {todo[i]['isp']} Capacidade: {todo[i]['data_capacity']} Velocidade de download: {todo[i]['download_speed']} |"
                       f" Velocidade de upload: {todo[i]['upload_speed']} Descrição {todo[i]['description']} Preço mensal: {todo[i]['price_per_month']}"
                       f" Tipo de internet: {todo[i]['type_of_internet']}")
    print(lista)
empresa()