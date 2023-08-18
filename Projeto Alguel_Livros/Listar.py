import os,csv
def listar_usuarios():
    os.system('cls') or None
    usuarios_csv = open('Usuarios.csv', encoding='utf-8') #abrindo arquivo
    dados_usuario = csv.DictReader(usuarios_csv, delimiter=";") #lendo o arquivo
    print("========== LISTAGEM DE USUÁRIOS ===========")
    print(f'{"CPF":15}', f'{"NOME":25}', "RG")
    for cliente in dados_usuario: #percorrendo as linhas do arquivo
        print(f'{cliente["CPF"]:15}', f'{cliente["NOME"]:25}', "RG")
    print("===========================================")
    usuarios_csv.close()
            

def listar_livros():
    livros_csv=open('Livros.csv',encoding='utf-8')#abrindo arquivo
    dados_livros=csv.DictReader(livros_csv, delimiter=";")#lendo o arquivo
    print("========== LISTAGEM DE LIVROS ===========")
    print(f'{"CODIGO":15}', f'{"ANO":15}', f'{"EDITORA":25}', f'{"NOME":25}', "AUTOR")
    for livros in dados_livros: #percorrendo as linhas do arquivo
        print(f'{livros["CODIGO"]:15}', f'{livros["ANO"]:15}', f'{livros["EDITORA"]:25}', f'{livros["NOME"]:25}', "AUTOR")
    print("=========================================")
    livros_csv.close()

def listar_emprestimo():
    emprestimo_csv=open('Emprestimo.csv',encoding='utf-8')#abrindo arquivo
    dados_emprestimo=csv.DictReader(emprestimo_csv, delimiter=";")#lendo o arquivo
    print("========== LISTAGEM DE EMPRESTIMOS ===========")
    print(f'{"CODIGO":15}', f'{"ANO":15}', f'{"EDITORA":25}', f'{"NOME_LIVRO":25}', f'{"AUTOR":25}', f'{"NOME_USUARIO":25}', f'{"CPF":15}', "DATA-EMPRESTIMO")
    for emprestimo in dados_emprestimo: #percorrendo as linhas do arquivo
        print(f'{emprestimo["CODIGO"]:15}', f'{emprestimo["ANO"]:15}', f'{emprestimo["EDITORA"]:25}', f'{emprestimo["NOME_LIVRO"]:25}', f'{emprestimo["AUTOR"]:25}', f'{emprestimo["NOME_USUARIO"]:25}', f'{emprestimo["CPF"]:15}', "DATA-EMPRESTIMO")
    print("==============================================")
    emprestimo_csv.close()