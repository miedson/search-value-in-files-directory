# Script para buscar valor em arquivos de texto

Este script busca um determinado valor dentro de uma coleção de arquivos de texto, por exemplo, quando existe a necessidade de buscar um nome especifico que pode estar em qualquer arquivo de texto dentre milhares em um diretório.

## Como usar
Para usar o script é muito simples, basta chama-lo em terminal passando o valor da pesquisa e a extensão dos arquivos de textos existentes no diretório.

![Exemplo de execução do script](https://i.imgur.com/Ixafp2A.png "Exemplo de execução do script")

Como pode ser observado na imagem acima, o resultado da busca é salvo em um novo arquivo de texto no mesmo diretório em que a busca esta sendo executada, chamado de saida.txt. Nele, será gravado o nome do arquivo e a linha de onde o valor foi encontrado. Abaixo, veja um exemplo com o resultado da busca:

    Arquivo:
     .\arquivo1.txt 
    
    Linha:
     industry. Lorem Ipsum valorbuscado has been the industry's standard dummy
    =========================================
    Arquivo:
     .\arquivo4.txt 
    
    Linha:
     of type and scrambled it to make a type specimen book. It has valorbuscado
    =========================================
    
    
**O script foi desenvolvido utilizando python3, sendo assim, é necessario ter o mesmo instalado!**
