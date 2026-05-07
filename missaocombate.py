from missao import Missao

class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, tipo_inimigo, inimigos_a_derrotar):
        super().__init__(nome, descricao, recompensa)
        self.__tipo_inimigo = tipo_inimigo
        self.__inimigos_a_derrotar = inimigos_a_derrotar

    def exibir_dados(self):
        return super().exibir_dados()
        print(f"Inimigo: {self.__tipo_inimigo}")
        print(f"Quantidade: {self.__inimigos_a_derrotar}")


