class Personagens:
    def __init__(self,nome:str):
        self.nome = nome
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0
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
    @nome.setter
    def nome(self, novo_nome:str):
        if novo_nome is None:
            raise Exception("nome é obrigatorio")
        self.__nome = novo_nome.title().strip()
    ##GANHA XP
    def ganha_xp(self, valor: int):
        if valor <=0:
             raise Exception("XP deve ser positivo")
        self.__xp += valor
    ##PERDE VIDA
    def perde_vida(self,valor: int):
        if valor <=0:
             raise Exception("Vida deve ser positivo")
        self.__vida -= valor
    ##aumenta a nivel
    def aumenta_nivel(self):
         self.__nivel +=1 

    def exibir_dados(self):
        return f"Nome: {self.nome}- Nivel: {self.__nivel}- Vida {self.__vida}- Xp{ self.__xp}"
    
    def __str__(self):
        return self.exibir_dados()
    
    def __eq__(self, outro):
        return isinstance(outro, Personagens) and self.nome == outro.nome
    