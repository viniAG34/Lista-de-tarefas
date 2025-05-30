# from models.tarefas import Tarefa  # Import relativo simples


# class Funcoes_tarefa:
#     lista_tarefas = []
#     proximo_id = 1

#     @classmethod
#     def salvar_tarefa(cls, titulo: str, descricao: str) -> Tarefa:
        
#         nova_tarefa = Tarefa(titulo, descricao, cls.proximo_id)
#         cls.lista_tarefas.append(nova_tarefa)
#         cls.proximo_id += 1
#         return nova_tarefa

#     @classmethod
#     def apresentar_tarefas(cls):
#         """imprime lista de tarefas"""
#         for i, tarefa in enumerate(cls.lista_tarefas, start=1):
#             print(f"{i}. {tarefa.titulo}")

#     @classmethod
#     def listar_tarefas(cls):
#         """retorna a lista de tarefas com titulo e descricao"""
#         return cls.lista_tarefas
    
#     @classmethod
#     def exibir_tarefas(cls):
#         if not cls.lista_tarefas:
#             print('nenhuma tarefa cadastrada')
#             return
        
#         print("\nLista de Tarefas:")
#         for tarefa in cls.lista_tarefas:    
#             status = 'ok' if Tarefa.status else " "
#             print(f"[{status}] #{Tarefa.id}: {Tarefa.titulo}")
#             if Tarefa.descricao:
#                 print(f"    Descrição: {Tarefa.descicao}")

#==============================================================================================================

import sys
import os
from pathlib import Path

# Adiciona o diretório src ao PATH
SRC_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SRC_DIR))

from models.tarefas import Tarefa

class Funcoes_tarefa:
    lista_tarefas = []
    proximo_id = 1

    @classmethod
    def salvar_tarefa(cls, titulo: str, descricao: str) -> Tarefa:
        nova_tarefa = Tarefa(titulo, descricao, cls.proximo_id)
        cls.lista_tarefas.append(nova_tarefa)
        cls.proximo_id += 1
        return nova_tarefa

    @classmethod
    def exibir_tarefas(cls):
        if not cls.lista_tarefas:
            print("Nenhuma tarefa cadastrada")
            return
            
        print("\nLista de Tarefas:")
        for tarefa in cls.lista_tarefas:
            status = "✓" if tarefa.status else " "
            print(f"[{status}] #{tarefa.id}: {tarefa.titulo}")
            if tarefa.descricao:
                print(f"   Descrição: {tarefa.descricao}")
