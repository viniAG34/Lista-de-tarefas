from controllers.tarefa_controller import Funcoes_tarefa
import sys
import os
from pathlib import Path

# Adiciona o diretório src ao PATH
SRC_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC_DIR))


def main():

    # Exibir tarefas

    # #scolha do usuario
    # opcao = int(input('escolha uma opção a seguir'))

    # match opcao:
    #     #adicionar nova tarefa
    #     case 1:
    #         entrada_titulo = input('digite o título da nota: ')
    #         entrada_descricao = input('digite a descrição da nota: ')

    #         Funcoes_tarefa.adicionar_tarefa(entrada_titulo, entrada_descricao)

    # Criar tarefas de exemplo
    tarefa1 = Funcoes_tarefa.adicionar_tarefa("Estudar Python", "Padrões MVC")
    tarefa2 = Funcoes_tarefa.adicionar_tarefa("Compras", "Leite, ovos, pão")

    Funcoes_tarefa.exibir_tarefas()
    # Marcar uma tarefa como concluída
    tarefa1.status = True


if __name__ == "__main__":
    main()
