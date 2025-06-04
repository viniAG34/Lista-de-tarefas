

class Tarefa:

    def __init__(self, titulo, descricao, id):
        self.titulo = titulo
        self.descricao = descricao
        self.id = id
        self.status = False

    def marcar_concluido(self):
        self.status = True
