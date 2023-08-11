import csv
def pesquisar_usuario(nome):
    usuarios_csv=open('Usuarios.csv')#abrindo arquivo
    dados_usuario=csv.DictReader(usuarios_csv, delimiter=";")#lendo o arquivo
    for cliente in dados_usuario:#percorrendo as linhas do arquivo
        if (cliente['NOME'].lower() == nome.lower()): #listar o nome do cliente, a partir da chave
            nome = cliente['NOME']
            cpf = cliente["CPF"]
            rg = cliente["RG"]
            return (True,nome,cpf,rg)
    return (False,)

        
def pesquisar_livro(cod):
    livros_csv = open('Livros.csv')
    dados_livro=csv.DictReader(livros_csv, delimiter= ";")
    for livro in dados_livro:
        if cod == livro["CODIGO"]:
            codigo = livro["CODIGO"]
            livro_nome = livro["NOME"]
            livro_ano = livro["ANO"]
            editora = livro["EDITORA"]
            autor = livro["AUTOR"]
            return (True, codigo, livro_nome,livro_ano,editora,autor)
    return (False,)