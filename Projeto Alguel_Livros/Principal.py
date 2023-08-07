import Cadastrar as c #apelido
import Listar,Emprestimo,Relatorio,Remover

resposta='s'
while(resposta=='s'):
    menu= '''============= BIBLIOTECA TDS 10 ==============="
    \r[1] Cadastrar Usuário
    \r[2] Listar Usuários
    \r[3] Cadastrar Livro
    \r[4] Listar Livros
    \r[5] Realizar Empréstimo
    \r[6] Listar Empréstimos
    \r[7] Relatório de livros atrasados
    \r[8] Remover Usuário
    \r[9] Remover Livro
    '''
    print(menu)
    opcao=int(input("Entre com uma opção: ")) #escolher opção digitada
    if(opcao==1):
        c.cadastro_usuario()
    elif(opcao==2):
        Listar.listar_usuarios()
    elif(opcao==3):
        c.cadastro_livro()
    elif(opcao==4):
        Listar.listar_livros()
    elif(opcao==5):
        Emprestimo.emprestimo()
    elif(opcao==6):
        Listar.listar_emprestimo()
    elif(opcao==7):
        Relatorio.relatorio()
    elif(opcao==8):
        Remover.remover_usuario()
    elif(opcao==9):
        Remover.remover_livro()
    
    resposta=input("\nDeseja continuar? [s] para sim, [n] para não: ")
