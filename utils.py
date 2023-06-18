import requests 
import re
from datetime import datetime, time
import time as t
from cnpjWS import ConsultaWS
from speedio import Speedio

urlConsultaWS = 'https://publica.cnpj.ws/cnpj/'
urlSpeedio ='https://api-publica.speedio.com.br/buscarcnpj?cnpj='

def validaCNPJ(cnpj=str):
    validaDigitosEPontos = re.search('^\d{2}.\d{3}.\d{3}/\d{4}-\d{2}$', cnpj)
    validaDigitos = re.search('^\d{14}$', cnpj)

    if(validaDigitosEPontos or validaDigitos):
        return True 
    else:
        print('CNPJ inválido! Tente novamente')
        return False

def consultaCNPJ(CNPJ=str, consulta=str):
    cnpj = CNPJ.replace('.', "").replace("/", "").replace("-", "")
    print(cnpj)
    if(consulta == 'speedio'):
        data = requests.get(f"{urlSpeedio}{cnpj}").json()
        company = Speedio(data)
        company.saveToFile()
    if(consulta == 'ws'):
        data = requests.get(f"{urlConsultaWS}{cnpj}")
        if data.status_code == 429:
            # public api has a cooldown of 3 minutes if you request 3 times in a minute
            for i in range(60,0,-1):
                print(f"{i} segundos restantes para poder utilizar novamente a API", end="\r", flush=True)
                t.sleep(1)
            data = requests.get(f"{urlConsultaWS}{cnpj}")
        company = ConsultaWS(data.json()) 
        company.saveToFile()
