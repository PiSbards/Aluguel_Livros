import csv
def pesquisar_usuario(nome):
    usuarios_csv=open('Usuarios.csv')#abrindo arquivo
    dados_usuario=csv.DictReader(usuarios_csv, delimiter=";")#lendo o arquivo
    for cliente in dados_usuario:#percorrendo as linhas do arquivo
        if nome.lower() == cliente["NOME"].lower(): # listar o nome do cliente, a partir da chave
            return cliente["NOME"],cliente["CPF"],cliente["RG"]
    return False
        
def pesquisar_livro(cod):
    livros_csv = open('Livros.csv')
    dados_livro=csv.DictReader(livros_csv, delimiter= ";")
    for livro in dados_livro:
        if cod == livro["CODIGO"]:
            return livro["CODIGO"],livro["NOME"], livro['ANO'],livro['EDITORA'], livro['AUTOR']
    return False