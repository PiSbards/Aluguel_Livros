import os,csv
import pequisar as p
import Cadastrar as c
from datetime import date
import datetime

def emprestimo():
    emprestimos=[]
    os.system('cls')
    print("============= EMPRESTIMO DE LIVRO =============")
    nomeUsuario=input("Digite o nome do usuário: ")
    retorno= p.pesquisar_usuario(nomeUsuario)
    if(retorno == False):
        c.cadastro_usuario()
    

    if(retorno[0]==True):
        codLivro=input("Digite o código do Livro: ")
        livro = p.pesquisar_livro(codLivro)        
        if(livro[0] == False):
            c.cadastro_livro()
            
        else:
            dataEmprestimo=date.today()  
        
    
        colunas=['CODIGO','ANO','EDITORA','NOME_LIVRO','AUTOR','NOME_USUARIO','CPF','DATA_EMPRESTIMO']
        file_exists = os.path.isfile('Emprestimo.csv')
        with open('Emprestimo.csv', 'a', newline='', encoding='utf-8') as emprestimo_csv:
            cadastrar = csv.DictWriter(emprestimo_csv, fieldnames=colunas, delimiter=';', lineterminator='\n\r')
            if not file_exists:
                cadastrar.writeheader()
            cadastrar.writerow({'CODIGO':livro[1],'ANO':livro[3],'EDITORA':livro[4],'NOME_LIVRO': livro[2],'AUTOR': livro[5],
                                'NOME_USUARIO':retorno[1],'CPF': retorno[2],'DATA_EMPRESTIMO':dataEmprestimo})
        print("Emprestimo realizado com sucesso!")
    else:
        print("Emprestimo realizado com sucesso!")