import sys
import os
import glob

if(len(sys.argv) == 3):
    valor = sys.argv[1]
    tipo = sys.argv[2]
    path = os.path.dirname(__file__)
    saida = open(path + '/saida.txt', 'w+')
    files = glob.glob(path + '/*.' + tipo)
    for file in files:
        arq = open(file, 'r', encoding='ANSI')
        for txt in arq.readlines():
            if valor in txt:
                saida.writelines(f'Arquivo:\n {file} \n\nLinha:\n {txt}')
                saida.writelines('=========================================\n')
                print(f'Ocorrência encontrada no arquivo: {file}')
        arq.close()
    print(
        f"Pesquisa concluida, arquivo com resultado encontra-se em: {path}/saida.txt")
    saida.close()
else:
    print("Falta passar o valor da pesquisa ou o tipo de arquivo após o script!")
