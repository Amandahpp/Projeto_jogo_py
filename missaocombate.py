from missao import Missao

class MissaoCombate(Missao):
    def __init__(self,
                 nome,
                 descricao,
                 recompensa,
                 tipo_inimigo,
                 inimigos_a_derrotar):

        super().__init__(nome, descricao, recompensa)

        self.__tipo_inimigo = tipo_inimigo
        self.__inimigos_a_derrotar = inimigos_a_derrotar

    def concluir_missao(self,derrotados):
        if derrotados >= self.__inimigos_a_derrotar:
            self.estado.concluir(self.recompensa)
        else:
            self.estado.concluir(0)
        
    def exibir_dados(self):
      return f"""
      {super().exibir_dados()}
      Inimigo: {self.__tipo_inimigo}
      Quantidade: {self.__inimigos_a_derrotar}"""