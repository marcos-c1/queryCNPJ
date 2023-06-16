from utils import validaCNPJ, consultaCNPJ 

if __name__ == '__main__':
    cnpj = str(input())
    while(not validaCNPJ(cnpj)):
        cnpj = str(input())
    consultaCNPJ(cnpj, consulta='ws')
