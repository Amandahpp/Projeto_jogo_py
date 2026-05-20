class Personagens:
    def __init__(self,nome:str,ataqueBase: float,vidaBase: int = 100):
        self.nome = nome
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0
        self.__missoes = []

        self.__ataqueBase = ataqueBase
        self.__inventario = []

        self.__arma= None
        self.__vestimenta= None
        self.__utilitario= None

    @property
    def nome(self):
        return self.__nome
    @property
    def nivel(self):
        return self.__nivel
    @property
    def vida(self):
        return self.__vida
    @property
    def xp(self):
        return self.__xp
    @property
    def missoes(self):
        return self.__missoes
    
    @nome.setter
    def nome(self, novo_nome:str):
        if novo_nome is None:
            raise Exception("nome é obrigatorio")
        self.__nome = novo_nome.title().strip()
    ##GANHA XP
    ##def ganha_xp(self, valor: int):
        ##if valor <=0:
            ## raise Exception("XP deve ser positivo")
        ##self.__xp += valor

    ##PERDE VIDA
    def perde_vida(self,valor: int):
        if valor <=0:
             raise Exception("Vida deve ser positivo")
        self.__vida = max(0, self.__vida - valor)
    ##aumenta a nivel
    def aumenta_nivel(self):
         self.__nivel +=1 

    ##INVENTARIO
    def add_item(self,item):
        self.__inventario.append(item)

    def remover_item(self,item):
        self.__inventario.remove(item)

    def mostrar_inventario(self,item):
        for item in self.__inventario:
            print(item)

    def equiparItens(self,item):
        if item.tipo.name == "ARMA":
            self.__arma = item
        elif item.tipo.name == "VESTIMENTA":
            self.__vestimenta = item
        elif item.tipo.name == "UTILITARIO":
            self.__utilitario = item
    

##terminar isso aqui
    def calculoStatus(self):
        bonus =0 
        if self.__vestimenta:
            bonus += self.__vestimenta.valorEfeito
        elif self.__utilitario:
            bonus += self.__utilitario.valorEfeito
        elif self.__arma:
            bonus += self.__arma.valorEfeito
        
        ataque_total = self.__ataqueBase + bonus

        return ataque_total
    ##MISSAO
    def adicionar_missao(self,missao):
        self.__missoes.append(missao)
        
    def listar_missoes(self):
        if len(self.__missoes) == 0:
            print("nenhuma missao encontrada")
            return
        print("\n ===== MISSOES =====")

        for i, m in enumerate(self.__missoes):
            print(f""" [{i}] {m.nome} Descrição: {m.descricao}Recompensa: {m.recompensa} XP Estado: {type(m.estado).__name__} """)

    def concluir_missao(self,nome_missao,valor = 1):
        for m in self.__missoes:
            if m.nome == nome_missao:
                m.conlcuir_missao(valor)
                return
        print("missao nao encontrada")

    def exibir_dados(self):
        return f"""
        ====== PERSONAGENS ======
        Nome: {self.nome} 
        Nivel: {self.__nivel} 
        Vida {self.__vida} 
        XP {self.__xp} 
        Ataque: {self.calculoStatus()}"""
    
    def __str__(self):
        return self.exibir_dados()
    
    def __eq__(self, outro):
        return isinstance(outro, Personagens) and self.nome == outro.nome
    

