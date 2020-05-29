# Buscador de valor em arquivos de texto

Este script busca um determinado valor dentro de uma coleção de arquivos de texto, por exemplo, buscar um nome especifico que pode estar em qualquer arquivo de texto em um determinado diretório.

## Como usar
Para usar o script é muito simples, basta chama-lo em terminal passando o valor da pesquisa e a extensão dos arquivos de textos existentes no diretório.

![Exemplo de execução do script](https://i.imgur.com/mjBZghW.png "Exemplo de execução do script")

Conforme pode ser visto na execução acima, o resultado da busca é salva em um novo arquivo de texto no mesmo diretorio em que a busca esta sendo executada chamado de saida.txt. Nele, será gravado o nome do arquivo e a linha de onde o valor foi encontrado. Abaixo veja um exemplo com o resultado da busca:

    Arquivo:
     .\arq1.txt 
    
    Linha:
     Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus textoexemplo1 Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32

**O script foi desenvolvido utilizando python3, sendo assim, é necessario ter o python3 instalado**
