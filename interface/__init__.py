def verificarInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: Por favor, digite um valor válido.')
            continue
        except(KeyboardInterrupt):
            print('ERRO: Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n

def line(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(line())
    print(txt.center(42))
    print(line())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(line())
    opc = verificarInt('Sua opção: ')
    return opc