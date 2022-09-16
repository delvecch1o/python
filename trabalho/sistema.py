from trabalho.lib.interface import *
from trabalho.lib.arquivo import *
from time import sleep
import os


arq = 'crud.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Alunos Cadastradas', 'Cadastrar um novo Aluno', 'Alterar dados', 'Excluir', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        id = leiaInt('ID: ')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        rg = leiaInt('RG: ')
        cadastrar(arq, id, nome, idade, rg)
    elif resposta == 3:
        cabeçalho('ATUALIZANDO CADASTRO')
        id = leiaInt('ID: ')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        rg = leiaInt('RG: ')
        alteraArquivo(arq, id, nome, idade, rg)
    elif resposta ==4:
        cabeçalho('Excluir')
        if os.path.exists("crud.txt"):
            os.remove("crud.txt")
            print("Arquivo deletado !")
        else:
            print("Arquivo não existe !")
    elif resposta ==5:
        cabeçalho('Saindo do sistema..')
        break
    else:
        print('ERRO ! Valor Incorreto')
    sleep(2)