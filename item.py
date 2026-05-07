from enum import Enum 
class TipoItem(Enum):
    ARMA = 1
    VESTIMENTA = 1
    UTILITARIO = 1


class Item():
    def __init__(self,nome,descricao,tipo,valorEfeito):
        self.nome=nome
        self.descricao=descricao
        self.tipo=tipo
        self.valorEfeito=valorEfeito

    def __str__(self):
        return f"{self.nome}({self.tipo.name})- Efeito: {self.valorEfeito}"
    