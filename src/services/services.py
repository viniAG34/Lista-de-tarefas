from models.models import Tarefa
from repository.repository import lista_tarefas


class Funcoes_tarefa:
    @classmethod
    def apresentar_tarefas(lista_tarefas):
        """imprime lista de tarefas"""
        for i, tarefa in enumerate(lista_tarefas, start=1):
            print(f"{i}. {tarefa.titulo}")

    @classmethod
    def numero_de_tarefas(cls):
        """retorna o número de tarefas na lista"""
        print(len(cls.lista_tarefas))

    
    