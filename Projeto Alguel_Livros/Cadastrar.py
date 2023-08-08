import os, csv
def cadastro_usuario():
    os.system('cls')#limpar tela
    dados={}#criando dicionário de dados, para armazenar usuários
    print("============== CADASTRO DE CLIENTES ===============")
    nome=input("Digite o seu nome: ")
    cpf=input("Digite o seu CPF:")
    rg=input("Digite o seu RG:")
    
    dados[cpf]=[nome,rg]
    colunas=['CPF','NOME','RG']

    files_exist = os.path.isfile('Usuarios.csv')

    with open('Usuarios.csv','a', newline="", encoding='utf-8') as usuarios_csv:
        cadastrar = csv.DictWriter(usuarios_csv, fieldnames=colunas,delimiter=";", lineterminator="\r\n")
        if (not files_exist):
            cadastrar.writeheader()
        cadastrar.writerow({"CPF":cpf, "NOME":nome, "RG":rg})

    print("Cadastro realizado com sucesso!")


def cadastro_livro():
    os.system('cls')
    dados={}
    print("============== CADASTRO DE LIVRO ================")
    codigo= int(input("Código:"))
    nome=input("Digite o seu título do livro: ")
    ano=input("Digite o ano de lançamento do livro: ")
    editora = input("Digite a editora: ")
    autor = input("Digite o Autor do livro: ")    
    
    dados[codigo]=[ano, editora, nome, autor]
    colunas=['CODIGO','ANO','EDITORA','NOME','AUTOR']

    files_exist = os.path.isfile('Livros.csv')

    with open('Livros.csv','a', newline="", encoding='utf-8') as livros_csv:
        cadastrar = csv.DictWriter(livros_csv, fieldnames=colunas,delimiter=";", lineterminator="\r\n")
        if (not files_exist):
            cadastrar.writeheader()
        cadastrar.writerow({"CODIGO":codigo,"ANO":ano,"EDITORA":editora, "NOME":nome, "AUTOR":autor})

    print("Cadastro realizado com sucesso!")