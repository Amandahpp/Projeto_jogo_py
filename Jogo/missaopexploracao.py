from missao import Missao

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa,regia_destino,distancia_em_km):
        super().__init__(nome, descricao, recompensa)
        self.__regiao_destino =regia_destino
        self.__distancia_em_km = distancia_em_km

    def exibir_dados(self):
        return super().exibir_dados()
        print(f"Destino: {self.__regiao_destino}")
        print(f"Distância: {self.__distancia_em_km} km")