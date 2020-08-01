from interface import *
from cadastro import *
from time import sleep
while True:
    resposta = menu(['Organizar','Sair'])
    if resposta == 1:
        cabecalho('Opção 1: ')
        organizar()
    elif resposta == 2:
        cabecalho('Saindo... Até logo')
        break
    else:
        print('ERRO: Por favor, escolha uma válido.')
        sleep(2)