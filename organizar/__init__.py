import os
import shutil
from interface import cabecalho
from time import sleep

pastas = []
arquivos = []
pasta = 'C:/Users/Robso/Desktop/SESI'

def organizar():
    ar = os.listdir(f'{pasta}')
    for file in ar:
        if os.path.isfile(f'{pasta}/{file}'):
            arquivos.append(file)
        else:
            pastas.append(file)
    for arquivo in arquivos:
        for folder in pastas:
            if arquivo.startswith(f'{folder}'):
                shutil.move(f'{pasta}/{arquivo}',f'{pasta}/{folder}')
                print(f'Movendo {arquivo} para {pasta}/{folder}')
                sleep(1)
    print("Fim da organização")