import sys
import os
from datetime import datetime

if(len(sys.argv) == 3):
    valor = sys.argv[1]
    tipo = sys.argv[2]
    path = os.path.abspath(__file__)[:os.path.abspath(__file__).rfind("\\") + 1]
    
    def insertDateTime(txt):
        datetimeNow = datetime.now()
        with open(f'{path}saida.txt', 'at') as arq:
            arq.write(f"{txt}{datetimeNow.strftime('%d/%m/%Y %H:%M')}\n\n")
            arq.close()

    def openFile(pathvalidated, dirs):
        count = 0
        for pathValid in pathvalidated:
            with open(pathValid, 'r', encoding='ANSI') as arq:
                for txt in arq.readlines():
                    if(valor in txt):
                        with open(f'{path}saida.txt', 'at') as saida:
                            saida.writelines(f'Local:\n {pathValid}\n\nLinha:\n {txt}')
                            saida.writelines('=========================================\n')
                            print(f'Ocorrência encontrada no arquivo: {pathValid}')
                        count += 1
                        saida.close()
            arq.close()
        if(count > 0):
            print(f'Busca concluida, foram encontrados um total de {count} ocorrência(s), o resultado encontra-se em {path}saida.txt')
            insertDateTime('\nFim: ')
        else:
            print(f'Não foi encontrado nenhuma ocorrência de {valor} nos diretorios: \n' + ', \n'.join(dirs))
            insertDateTime(f'Não foi encontrado nenhuma ocorrência de {valor} nos diretorios: \n' + ', \n'.join(dirs) + '\n\nFim: ')

    def verifyFile(files, dirs):
        pathvalidated = []
        for file in files:
            for dir in dirs:
                if os.path.exists(f'{dir}\{file}'):
                    pathvalidated.append(f'{dir}\{file}')
        openFile(pathvalidated, dirs)

    def scanDir(path):
        arr = []
        dirs = []
        if os.path.exists(f'{path}saida.txt'):
            os.remove(f'{path}saida.txt')
        insertDateTime('Inicio: ')
        for files in os.walk(path):
            dirs.append(files[0])
            for file in files[2]:
                if(os.path.splitext(file)[1] == f'.{tipo}'):
                    arr.append(file)
        verifyFile(arr, dirs)


    scanDir(path)

else:
    print("Falta passar o valor da pesquisa ou o tipo de arquivo após o script!")
