class funcionarios:
    def __init__(self,Nome,Onibus):
        self.Nome = Nome
        self.Onibus = Onibus
    def toSTRf(self):
        return f'{self.Nome} {self.Onibus}'
class Motorista:
    motoristas = []
    def adicionarMotorista(self,object):
        self.motoristas.append(object)
        print(f'motorista criado com sucesso')
##para selecionar somente um dos atributos fazer como .lista[n][1 ou 0]
class Fiscal:
    fiscais = []
    def adicionarFiscal(self,object):
        self.fiscais.append(object)
        print(f'Fiscal adicionado com sucesso')
class onibus:
    Onibus = []
    def __init__(self,Identificacao,Parada,Motorista,Fiscal):
        self.Identificacao = Identificacao
        self.Parada = Parada
        self.Motorista = Motorista
        self.Fiscal = Fiscal
    def toSTRo(self):
        return (f'{self.Identificacao} {self.Parada} {self.Motorista} {self.Fiscal}')
    def AdicionarOnibus(self,object):
        self.Onibus.append(object)
        print(f'onibus criado com sucesso')
class paradas:
    pontos = []
    def __init__(self,Pontos,Onibus):
        self.Pontos = Pontos
        self.Onibus = Onibus
    def toSTRp(self):
        return f'{self.Pontos} {self.Onibus}'
    def Novaparada(self,object):
        self.pontos.append(object)
        print(f'ponto criado com sucesso')
        
