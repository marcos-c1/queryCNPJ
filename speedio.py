class Speedio:
    def __init__(self, data):
        self.json = data
        self.nomeFantasia = data.get('NOME FANTASIA') 
        self.razaoSocial = data.get('RAZAO SOCIAL') 
        self.cnpj = data.get('CNPJ') 
        self.status = data.get('STATUS') 
        self.setor = data.get('SETOR') 
        if(self.setor is None):
            self.setor = data.get('CNAE PRINCIPAL DESCRICAO')
        self.cep = data.get('CEP') 
        if(data.get('DDD') != None and data.get('TELEFONE') != None):
            self.telefone = data.get('DDD') + data.get('TELEFONE') 
        else:
            self.telefone = None
        self.email = data.get('EMAIL')
        self.tipoLogradouro = data.get('TIPO LOGRADOURO') 
        self.logradouro = data.get('LOGRADOURO') 
        self.numero = data.get('NUMERO') 
        self.complemento = data.get('COMPLEMENTO') 
        self.bairro = data.get('BAIRRO') 
        self.municipio = data.get('MUNICIPIO') 
        self.uf = data.get('UF') 

    def _getURL(self):
        return self.url

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
        return self.telefone

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
        return f'{self.logradouro}, {self.tipoLogradouro} {self.numero}, {self.complemento}. {self.bairro}'

    def printData(self):
        print(f'{self.json}')

    def saveToFile(self):
        with open(f'./consultas/{self.razaoSocial}.speedio', "w+") as file:
            file.write(f'Razão Social: {self.razaoSocial}\n')
            file.write(f'Nome Fantasia: {self.nomeFantasia}\n')
            file.write(f'Bairro: {self.bairro}\n')
            file.write(f'CEP: {self.cep}\n')
            file.write(f'Cidade: {self.municipio}\n')
            file.write(f'UF: {self.uf}\n')
            file.write(f'Telefone: {self.telefone}\n')
            file.write(f'Email: {self.email}\n')
            file.write(f'CNPJ: {self.cnpj}\n')
            file.write(f'Ramo de atividades: {self.setor}\n')
        file.close()
        print(f"{self.razaoSocial} concluído!")

