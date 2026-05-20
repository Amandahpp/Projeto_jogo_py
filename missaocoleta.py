from missao import Missao

class MissaoColeta(Missao):
    def __init__(self,
                 nome,
                 descricao,
                 recompensa,
                 item_necessario,
                 qntd_item):

        super().__init__(nome, descricao, recompensa)

        self.__item_necessario = item_necessario
        self.__qntd_item = qntd_item
    def concluir_missao(self,quantidade):
        if quantidade >= self.__qntd_item:
            self.estado.concluir(self.recompensa)
        else:
            self.estado.concluir(0)
    
    def exibir_dados(self):
      return f"""
      {super().exibir_dados()}
      Item: {self.__item_necessario}
      Quantidade: {self.__qntd_item}"""