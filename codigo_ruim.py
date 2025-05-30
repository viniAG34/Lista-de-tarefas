# Bem vamos lá desenvolver algo kkk


# Lista base
lista_de_tarefas = []

# Evitar usar while para nao causar processamento infinito.

 # Visualização da lista
 estrela = '-'*30
  print('    LISTA-DE-TAREFAS   ')
   if lista_de_tarefas == ['']:
        print('     Lista vazia')
    else:
        for tarefa in lista_de_tarefas:
            print(lista_de_tarefas.index(tarefa)+1, tarefa, sep='-')
# usar operador logico para tratar

# Estabelecer menu onde há as opções:
# (lista exibida)
# 1. add a item to list
# 2. Remove a item of list
# 3. Limpar lista
    print(estrela)
    print('  Menu Lista de Tarefas')
    print('')
    print("Opções disponíveis:")
    menu = ['Adicionar uma tarefa',
            'Remover uma tarefa', 'Limpar a lista', 'Fechar']
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")
    opcao = int(input('O que deseja fazer?: '))

# Passar  parametro do input como uma variavel transformar para inteiro
# fazer um switch case
# criar função para chamar função quando chamar fnução
# usar case para evitar repetir tratamento de erro
# dividir os ifs em funções

    match opcao:

        # Preencher a lista
        case 1:
            while True:
                tarefa_add = input('escreva a tarefa a ser adicionada: ')
                if tarefa_add == '':
                    print('Sua tarefa está vazia')
                else:
                    lista_de_tarefas.append(tarefa_add)
                    print('tarefa adicionada')
                    Tarefa_adicional = input(
                        'deseja adicionar mais tarefas, sim ou não: ')
                    if Tarefa_adicional == 'sim':
                        print('adicione mais tarefas: ')
                    elif Tarefa_adicional == 'nao':

                 # Alteração da lista
        case 2:
            while True:
                print('    LISTA-DE-TAREFAS   ')
                for tarefa in lista_de_tarefas:
                    print(lista_de_tarefas.index(tarefa)+1, tarefa, sep='-')
                opcao_delete = input(
                    'Informe o número da tarefa que deseja excluir: ')
                if opcao_delete == '':
                    print('Opção inválida, tente de novo')
                else:
                    decisao = input(
                        'deseja realmente limpar a lista de tarefas? sim ou não: ')
                    if decisao == 'sim':
                        indice_deletado = int(opcao_delete)-1
                        lista_de_tarefas.pop(indice_deletado)
                        print('tarefa deletada')
                    elif decisao == 'nao':
                        print('opção invalida')
                    elif decisao == str:
                        print('opção invalida')

        # Limpar lista
        case 3:
            decisao = input(
                'deseja realmente limpar a lista de tarefas? sim ou não: ')
            if decisao == 'sim':
                lista_de_tarefas.clear()
            elif decisao == 'nao':
                print('opção invalida')
            elif decisao == str:
                print('opção invalida')

        case _:
            print('opção invalida')
