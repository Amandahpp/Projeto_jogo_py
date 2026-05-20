from missao import Missao

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa,regia_destino,distancia_em_km):
        super().__init__(nome, descricao, recompensa)
        self.__regiao_destino =regia_destino
        self.__distancia_em_km = distancia_em_km

    def concluir_missao(self, distancia_percorrida):

        if distancia_percorrida >= self.__distancia_em_km:

            self.estado.concluir(self.recompensa)

        else:

            self.estado.concluir(0)

    def exibir_dados(self):
          return f"""
          {super().exibir_dados()}

          Destino: {self.__regiao_destino}
          Distância: {self.__distancia_em_km} km"""