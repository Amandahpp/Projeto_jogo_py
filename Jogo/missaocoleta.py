from missao import Missao

class MissaoColeta(Missao):
    def __init__(self, nome, descricao, recompensa,item_necessario,qntd_item):
        super().__init__(nome, descricao, recompensa)
        self.__item_necessario = item_necessario
        self.__qntd_item = qntd_item

    def exibir_dados(self):
        return super().exibir_dados()
        print(f"Item: {self.__item_necessario}")
        print(f"Quantidade: {self.__quantidade_item}")