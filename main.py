from initialize.reader import *
from initialize.writer import *

def menu():
    print('\nLocalização de facilidades:\n')
    print('[1] - Visualizar Datasets')
    print('[2] - Armazenar resultados')
    print('[0] - Sair')


if __name__ == '__main__':
    menu()
    option = int(input('Digite a opção: '))
    while option != 0:
        if option == 1:
            print('\nVizualizar:\n')
            print('[0] - Todos')
            print('[1 - 5] - Escolha um arquivo específico')
            index = int(input('Digite a opção: '))
            if index == 0:
                readAllFiles()
            else:
                readFileByIndex(index)
        elif option == 2:
            for index in range(1, 6):
                data = readDatasets('pmed',index)
                writeResult(data,index)
            print('\nDados armazenados com sucesso!\n')
        else:
            print('Opção invalida')
        menu()
        option = int(input('Digite a opção: '))
