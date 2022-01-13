from classes import funcionarios
from classes import Motorista
from classes import Fiscal
from classes import onibus
from classes import paradas
'''sistema simples de gerenciamento para ser usado por uma rede de transporte, através dele, o
    usuario deve ser capaz de gerenciar  onibus, funcionarios e paradas. O programa deve premitir 
    que o usuario realize acoes pelo terminal. E, o sistema deve possuir as seguintes funcionalidades:
    ----Criar onibus, ponto de parada, motorista e fiscal;#
    ----Mostrar onibus, rotas, motoristas e fiscais;#
    ----assignar motorista ao onibus, fiscal ao onibus;#
    ----adicionar ponto de parada ao onibus;
    ----alterar dados do onibus, da parada, do motorista e do fiscal;#
    ----deletar onibus, ponto de parada, motorista e fiscal;#
    ----sair do programa.#
    **Considere que: as paradas são feitas em ordem; vários ônibus podem parar
    em um mesmo ponto, mas um ônibus não pode parar mais de uma vez em
    qualquer ponto; cada ônibus tem um motorista e nem sempre um fiscal;
    Um motorista não pode dirigir mais de um ônibus, igual com o fiscal; e o
    valor da passagem de cada ônibus é proporcional à rota do ônibus.'''
def programa():
    n = (int(input("digite o digito para a opcao que voce escolhe\
    1 - criar\
    2 - mostrar\
    3 - assignar\
    4 - alterar\
    5 - deletar\
    6 - adicionar\
    7 - valores\
    8 - Sair do Programa\
    ")))
    if n == 1:
    ##Criar alguma das opcoes
        c = int(input("digite a opcao que deseja criar\
            1 - onibus\
            2 - ponto de parada\
            3 - motorista\
            4 - fiscal\
            "))
        if c ==1:
        #onibus
            Identificacao = input("identificacao")
            Parada = input("Paradas")
            Motorista = input("motorista")
            Fiscal = input("fiscal")
            Novoonibus = onibus(Identificacao, Parada, Motorista, Fiscal)
            a = onibus()
            a.onibus.AdicionarOnibus(Novoonibus())
        elif c ==2:
        #paradas
            Ponto = input("ponto") 
            Onibus = input("Onibus")
            Novoponto = paradas(Pontos,Onibus)
            a = paradas()
            a.Novaparada(Novoponto)
        elif c == 3:
        #motoristas
            Nome = input("nome?    ")
            Onibus = input("Onibus?  ")
            Novomotorista = funcionarios(Nome, Onibus)
            a = Motorista()
            a.adicionarMotorista(Novomotorista)
        else:
        #fiscais
            Nome = input("nome?    ")
            Onibus = input("Onibus?  ")
            NovoFiscal = funcionarios(nome, Onibus)
            a = Fiscal()
            a.adicionarFiscal(NovoFiscal)
    elif n ==2:
    ## Mostrar alguma das opcoes
        escolha = int(input("digite qual opcao deseja mostra\
            1 - onibus\
            2 - fiscais\
            3 - rotas\
            4 - motoristas"))
        if escolhas == 1:
            print(a.Onibus)
        elif escolhas == 2:
            print(a.fiscais)
        elif escolhas ==3:
            print(a.pontos)
        else:
            print(a.motoristas)
    elif n ==3:
    ##Assignar motorista ao onibus  ou fiscal ao onibus
        escolha = int(input("digite qual funcionario deseja assignar a algum onibus\
        1 - motorista\
        2 - fiscal"))
        if escolhas == 1:
            m = int(input('digite em qual posicao esta o motorista de sua escolha'+print(a.motoristas)))
            o = int(input('digite em qual posicao esta o onibus de sua escolha'+print(a.Onibus)))
            motoristas[m][1] = Oninbus[o][2]
            Onibus[o][2] = motorista[m][1]
        else:
            f = int(input('digite em qual posicao esta o fiscal de sua escolha'+print(a.fiscais)))
            o = int(input('digite em qual posicao esta o onibus de sua escolha'+print(a.Onibus)))
            fiscais[m][1] = Oninbus[o][3]
            Onibus[o][3] = fiscais[m][1]
    elif n== 4:
    ##alterar algum do atributo do onibus, paradas, motorista ou fiscal
        escolha = int(input("digite qual objeto deseja alterar\
        1 - onibus\
        2 - parada\
        3 - motorista\
        4 - fiscal"))
        if escolha ==1:
            o = int(input('digite em qual posicao esta o onibus que deseja alterar'+print(a.Onibus)))
            alteracao = int(input("digite a posicao da informacao que deseja alterar\
                1 - identificacao\
                2 - rota\
                3 - motorista\
                4 - fiscal"))
            if alteracao == 1:
                Novaid = input("qual e a nova identificacao do onibus?")
                Onibus[o][0] = Novaid
            elif alteracao ==2:
                Novarota = input("qual e a nova rota?")
                Onibus[o][1] = Novarota
            elif alteracao ==3:
                Novomotor = input("qual o novo motorista?")
                Onibus[o][2] = Novomotor
            else:
                Novofiscal = input("qual e o novo fiscal?")
        elif escolha ==2:
            print(a.pontos)
            escolha = int(input("digite qual ponto deseja alterar"))
            novoPonto = input("digite o novo ponto")
            pontos[escolha] = novoPonto
        elif escolha ==3:
            print(a.motoristas)
            escolha = int(input("em qual posicao esta o motorista que deseja alterar"))
            alteracao = int(input("digite em qual posicao esta o dado que deseja alterar\
                1 - nome\
                2 - onibus"))
            if alteracao == 1:
                Novonome = input("qual o novo nome desse motorista")
                motoristas[escolha][0] = Novonome
            else:
                print(a.Onibus)
                Novoonibus = input("qual o novo onibus?")
                motorista[escolha][1] = novoonibus
        else:
            print(a.fiscais)
            escolha = int(input("em qual posicao esta o fiscal que deseja alterar"))
            alteracao = int(input("digite em qual posicao esta o dado que deseja alterar\
                1 - nome\
                2 - onibus"))
            if alteracao == 1:
                Novonome = input("qual o novo nome desse fiscal")
                fiscais[escolha][0] = Novonome
            else:
                print(a.Onibus)
                Novoonibus = input("qual o novo onibus?")
                fiscais[escolha][1] = novoonibus
    elif n==5:
    ##deletar o onibus ou ponto de parada pu motorista ou fiscal
        escolha = int(input("digite qual objeto deseja deletar\
            1 - onibus\
            2 - parada\
            3 - motorista\
            4 - fiscal"))
        if escolha==1:
            print(a.Onibus)
            deletar= int(input("digite a posicao do onibus que deseja deletar"))
            del(onibus[deletar])
        elif escolha ==2:
            print(a.pontos)
            deletar = int(input("digite qual ponto deseja deletar"))
            del(pontos[deletar])
        elif escolha==3:
            print(a.motoristas)
            deletar= int(input("digite a posicao do motorista que deseja deletar"))
            del(motorista[deletar])
        else:
            print(a.fiscais)
            deletar= int(input("digite a posicao do fiscal que deseja deletar"))
            del(fiscais[deletar])
    elif n==6:
    ##adicionar ponto de parada ao onibus
        print(a.Onibus)
        escolha = int(input("digite a posicao do onibus que deseja adiciona uma parada"))
        novaParada = input("digite a parada que desejaadicionar") 
        if novaParada not in pontos:
            print("essa parada nao existe")
            novaParada = input("digite a parada que deseja adicionar")
            Onibus[escolha][1] = Onibus[escolha][1]+ [novaParada]
        else:
            Onibus[escolha][1] = Onibus[escolha][1] +[novaParada]
    elif n==7:
    ##
        print(a.Onibus)
        escolha = input("digite sobre qual onibus deseja saber o valor da rota")
        valor = len(Onibus[escolha][1])
    else:
    ##sair do programa
        print('concluido')
        quit
        j = input("deseja continuar no programa? s/n\
            ")
        if j == 's':
            programa()
        else:
            print("concluido")
print(programa())
