# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


veiculoReg = namedtuple("veiculoReg", "matricula, carga, proximainspeccao, custokm")
listaveiculos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaveiculos)):
        if listaveiculos[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_veiculo():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o veiculo? ")
    
    registo = veiculoReg(cod, nome)
    listaveiculos.append(registo)


def pesquisar_veiculo():
    cod = input("Qual o codigo do veiculo a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhum veiculo com esse código"
        return

    print "Código: ", listaveiculos[pos].id
    print "Nome: ", listaveiculos[pos].nome
    


def listar_veiculos():
    for i in range (len(listaveiculos)):
        print "Matricula: ", listaveiculos[i].matricula
        print "Nome: ", listaveiculos[i].nome
        print
        print
        print
        
  

def eliminar_aluno():
    cod = input ("Código do veiculo a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhum veiculo com esse código"
        return

    # TODO: Confirmar eliminação
    listaveiculos.pop(pos)


    
def alterar_veiculo():
    cod = input ("Código do veiculo a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe nenhum veiculo com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listaveiculos[pos] = listaveiculos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.veiculos()

        if op == '1':
            inserir_veiculo()
        elif op =='2':
            listar_veiculos()
        elif op == '3':
            pesquisar_veiculo()
        elif op == '4':
            alterar_veiculo()
        elif op == '5':
            eliminar_aluno()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










