from utils import validaCNPJ, consultaCNPJ 
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=False, help="Arquivo contendo todos os cnpjs separados por linha")
    parser.add_argument("-c", "--cnpj", required=False, help="Passa o cnpj como argumento")
    parser.add_argument("-t", "--type", required=True, help="Recebe o tipo da consulta (ws || speedio)")

    args = parser.parse_args()

    f = args.file
    cnpj = args.cnpj
    typ = args.type

    if(cnpj):
        while(not validaCNPJ(cnpj)):
            cnpj = str(input())
        consultaCNPJ(cnpj, consulta=typ)
    elif(f):
        with open(f, "r") as file:
            cnpjs = file.read().strip()
            arr = cnpjs.split('\n')
            for cn in arr:
                consultaCNPJ(cn, consulta=typ)
        file.close()
    else:
        raise Exception("Argumento inválido")
