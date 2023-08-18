import csv,os
import pequisar
from datetime import datetime
def relatorio():
    emprestimos_csv = open('Emprestimo.csv')
    dados_emprestimo = csv.DictReader(emprestimos_csv,delimiter=';')
    os.system('cls') or None
    print("=============================================== RELATÓRIO DE EMPRESTIMOS ATRASADOS ======================================================")
    print(f'{"CODIGO":15}', f'{"ANO":15}', f'{"EDITORA":15}', f'{"NOME_LIVRO":15}', f'{"AUTOR":15}', f'{"NOME_USUARIO":15}', f'{"CPF":15}', f'{"EMPRESTIMO":15}', f'{"SITUAÇÃO"}')
    for emprestados in dados_emprestimo:
        data_emprestimo = datetime.strptime(emprestados['DATA_EMPRESTIMO'], '%Y-%m-%d')
        data_hoje = datetime.today()
        dias_atrasados = (data_hoje - data_emprestimo).days
        if dias_atrasados > 7:
            situacao = "Atrasado"
            print(f'{emprestados["CODIGO"]:15}',
                         f'{emprestados["ANO"]:15}',
                           f'{emprestados["EDITORA"]:15}',
                             f'{emprestados["NOME_LIVRO"]:15}',
                               f'{emprestados["AUTOR"]:15}',
                                 f'{emprestados["NOME_USUARIO"]:15}',
                                   f'{emprestados["CPF"]:15}',
                                     f'{emprestados["DATA_EMPRESTIMO"]:15}',
                                     situacao,
                                     dias_atrasados)



relatorio()