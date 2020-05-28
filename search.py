import sys
import os
import glob

if(len(sys.argv) == 3):
    valor = sys.argv[1]
    tipo = sys.argv[2]
    path = os.path.dirname(__file__)
    files = glob.glob(path + '/*.' + tipo)
    for file in files:
        arq = open(file, 'r')
        for txt in arq.readlines():
            if valor in txt:
                saida = open(path + '/saida.txt', 'w+')
                saida.writelines(file)
                saida.close()
        arq.close()

else:
    print("Falta passar o valor da pesquisa ou o tipo de arquivo após o script!")