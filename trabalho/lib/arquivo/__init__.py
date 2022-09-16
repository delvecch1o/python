from trabalho.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # Le um arquivo de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # escreve um arquivo de texto , se não existir o arquivo o "+" ira escrever.
        a.close()
    except:
        print('ERRO na criação do arquivo!')
    else:
        print(f'Aluno(a) {nome} foi cadastrado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('### Listagem ###')
        for linha in a:
            dado = linha.split(';')
            dado[3] = dado[3].replace('\n', '')
            print(f'{dado[0]:<5}{dado[1]:<20}{dado[2]:<10}{dado[3]:<10}')
    finally: # dando certo ou errado ira fechar o arquivo
        a.close()


def cadastrar(arq, id=0 , nome='desconhecido', idade=0, rg=0):
    try:
        a = open(arq, 'at') # o "a" é um append para colocar coisas dentro do arquivo
    except:
        print('ERRO na abertura do arquivo! ')
    else:
        try:
            a.write(f'{id};{nome};{idade};{rg}\n')
        except:
            print('ERRO na hora de escrever os dados! ')
        else:
            print(f'O aluno {nome} foi cadastrado com sucesso.')
            a.close()

def alteraArquivo(arq, id=0 , nome='desconhecido', idade=0, rg=0):
    try:
        w = open(arq, 'w+')
    except:
        print('ERRO na abertura do arquivo! ')
    else:
        try:
            w.write(f'{id};{nome};{idade};{rg}\n')
        except:
            print('ERRO na hora de escrever os dados! ')
        else:
            print(f'O aluno {nome} foi alterado com sucesso.')
            w.close()