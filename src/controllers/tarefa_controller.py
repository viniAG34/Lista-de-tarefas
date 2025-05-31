from models.tarefas import Tarefa
import sys
import os
from pathlib import Path

# Adiciona o diretório src ao PATH
SRC_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SRC_DIR))


class Funcoes_tarefa:
    # lista de armazenamento
    lista_tarefas = []
    # controle de indice
    proximo_id = 1

    @classmethod
    def adicionar_tarefa(cls, titulo: str, descricao: str) -> Tarefa:
        """adiciona tarefas a lista"""
        nova_tarefa = Tarefa(titulo, descricao, cls.proximo_id)
        cls.lista_tarefas.append(nova_tarefa)
        cls.proximo_id += 1
        return nova_tarefa

    @classmethod
    def apresentar_tarefas(cls):
        """imprime lista de tarefas"""
        for i, tarefa in enumerate(cls.lista_tarefas, start=1):
            print(f"{i}. {tarefa.titulo}")

    @classmethod
    def remover_tarefa(cls):
        """Remove uma tarefa da lista"""
        for i, tarefa in enumerate(cls.lista_tarefas, start=1):
            print(f"{i}. {tarefa.titulo}")
        opcao = int(input('informe o número da tarefa que deseja remover: '))
        cls.lista_tarefas.pop(opcao)

    @classmethod
    def numero_de_tarefas(cls):
        """retorna o número de tarefas na lista"""
        print(len(cls.lista_tarefas))

    @classmethod
    def exibir_tarefas(cls):
        """exibe as tarefas e suas descrições"""
        if not cls.lista_tarefas:
            print("Nenhuma tarefa cadastrada")
            return

        print("\nLista de Tarefas:")
        for tarefa in cls.lista_tarefas:
            status = "ok" if tarefa.status else " "
            print(f"[{status}] #{tarefa.id}: {tarefa.titulo}")
            if tarefa.descricao:
                print(f"Descrição: {tarefa.descricao}")
