class ConsultaWS:
    def __init__(self, data):
        self.razaoSocial = data['razao_social']
        self.nomeFantasia = data['estabelecimento']['nome_fantasia']
        self.cnpj = data['estabelecimento']['cnpj']
        self.bairro = data['estabelecimento']['bairro']
        self.cidade = data['estabelecimento']['cidade']['nome']
        self.cep = data['estabelecimento']['cep']
        self.uf = data['estabelecimento']['estado']['sigla']
        if(data['estabelecimento']['ddd1'] != None and data['estabelecimento']['telefone1']): 
            self.telefone = data['estabelecimento']['ddd1'] + data['estabelecimento']['telefone1']
        else:
            self.telefone = None
        self.email = data['estabelecimento']['email']
        self.ramo = data['estabelecimento']['atividade_principal']['descricao']
        inscricoes = data['estabelecimento']['inscricoes_estaduais']
        for i in range(len(inscricoes)):
            if(inscricoes[i]['estado']['sigla'] == self.uf):
                self.ie = inscricoes[i]['inscricao_estadual']
        
    def saveToFile(self):
        with open(f"./consultas/{self.razaoSocial}.ws", "w+") as f:
            f.write(f"Razão Social: {self.razaoSocial}\n")
            f.write(f"Nome Fantasia: {self.nomeFantasia}\n")
            f.write(f"Bairro: {self.bairro}\n")
            f.write(f"CEP: {self.cep}\n")
            f.write(f"Cidade: {self.cidade}\n")
            f.write(f"UF: {self.uf}\n")
            f.write(f"Telefone: {self.telefone}\n")
            f.write(f"E-mail: {self.email}\n")
            f.write(f"CNPJ: {self.cnpj}\n")
            f.write(f"IE: {self.ie}\n")
            f.write(f"Ramo de atividades: {self.ramo}")
        f.close()
        print(f"{self.razaoSocial} concluído!")
