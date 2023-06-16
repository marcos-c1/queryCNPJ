import requests
import re

class Company:
    def __init__(self, data):
        self.json = data
        self.nomeFantasia = data["NOME FANTASIA"] 
        self.razaoSocial = data["RAZAO SOCIAL"] 
        self.cnpj = data["CNPJ"] 
        self.status = data["STATUS"] 
        self.setor = data["SETOR"] 
        self.cep = data["CEP"] 
        self.ddd = data["DDD"] 
        self.telefone = data["TELEFONE"] 
        self.tipoLogradouro = data["TIPO LOGRADOURO"] 
        self.logradouro = data["LOGRADOURO"] 
        self.numero = data["NUMERO"] 
        self.complemento = data["COMPLEMENTO"] 
        self.bairro = data["BAIRRO"] 
        self.municipio = data["MUNICIPIO"] 
        self.uf = data["UF"] 

    def _getFantasia(self):
        return self.nomeFantasia

    def _getRazaoSocial(self):
        return self.razaoSocial

    def _getCNPJ(self):
        return self.cnpj
    
    def _getStatus(self):
        return self.ativa

    def _getSetor(self):
        return self.setor

    def _getCEP(self):
        return self.cep

    def _getTelefone(self):
        return self.ddd + self.telefone

    def _getEmail(self):
        return self.email

    def _getTipoLogradouro(self):
        return self.tipoLogradouro

    def _getLogradouro(self):
        return self.logradouro

    def _getNumero(self):
        return self.numero

    def _getComplemento(self):
        return self.complemento

    def _getBairro(self):
        return self.bairro

    def _getMunicipio(self):
        return self.municipio

    def _getUF(self):
        return self.uf

    def _getEndereco(self):
        return f"{self.logradouro}, {self.tipoLogradouro} {self.numero}, {self.complemento}. {self.bairro}"

    def printData(self):
        print(f"{self.json}")

def validaCNPJ(cnpj=str):
    validaDigitosEPontos = re.search('^\d{2}.\d{3}.\d{3}/\d{4}-\d{2}$', cnpj)
    validaDigitos = re.search('^\d{14}$', cnpj)

    if(validaDigitosEPontos or validaDigitos):
        return True 
    else:
        print("CNPJ inválido! Tente novamente")
        return False

def consultaCNPJ(cpnj=str):
    url = f'https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}'
    data = requests.get(url).json()

    company = Company(data)
    company.printData()
    
if __name__ == '__main__':
    cnpj = str(input())
    while(not validaCNPJ(cnpj)):
        cnpj = str(input())
    consultaCNPJ(cnpj)
