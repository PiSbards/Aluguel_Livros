import os
import pequisar as p
import Cadastrar as c
from datetime import date
import datetime
def emprestimo():
    emprestimos=[]
    os.system('cls')
    print("============= EMPRESTIMO DE LIVRO ============")
    nomeUsuario=input("Digite o nome do usuário: ")
    usuario= p.pesquisar_usuario(nomeUsuario)
    if(usuario == False):
        c.cadastro_usuario()
    
    codLivro=input("Digite o código do Livro: ")
    livro = p.pesquisar_livro(codLivro)
    if(livro==False):
        c.cadastro_livro()
    else:
        print(livro)
    
    #dataEmprestimo = 
    
    colunas=['CODIGO','ANO','EDITORA','NOME','AUTOR','DATA-EMPRESTIMO']

    