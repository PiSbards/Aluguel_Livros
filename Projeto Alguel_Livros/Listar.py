import os,csv
def listar_usuarios():
    usuarios_csv=open('Usuarios.csv')#abrindo arquivo
    dados_usuario=csv.DictReader(usuarios_csv, delimiter=";")#lendo o arquivo
    for cliente in dados_usuario:#percorrendo as linhas do arquivo
        print(cliente)
            

def listar_livros():
    livros_csv=open('Livros.csv')#abrindo arquivo
    dados_livros=csv.DictReader(livros_csv, delimiter=";")#lendo o arquivo
    for elemento in dados_livros:#percorrendo as linhas do arquivo
        print(elemento)

def listar_emprestimo():
    livros_csv=open('Emprestimo.csv')#abrindo arquivo
    dados_livros=csv.DictReader(livros_csv, delimiter=";")#lendo o arquivo
    for elemento in dados_livros:#percorrendo as linhas do arquivo
        print(elemento)