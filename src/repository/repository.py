from models.models import Tarefa

#eco %cd% -> retorna o caminho da pasta no win

# lista de armazenamento

class DadosTarefas:
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
    def remover_tarefa(cls):
        """Remove uma tarefa da lista"""
        for i, tarefa in enumerate(cls.lista_tarefas, start=1):
            print(f"{i}. {tarefa.titulo}")
        opcao = int(input('informe o número da tarefa que deseja remover: '))
        cls.lista_tarefas.pop(opcao)

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
