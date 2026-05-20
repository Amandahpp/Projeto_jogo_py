from status import EstadoPendente

class Missao:
    def __init__(self,nome:str, descricao:str, recompensa:int):
        self.__nome = ""       
        self.__descricao = ""
        self.__recompensa = 0

        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.__estado = EstadoPendente(self)
    @property
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, novo_estado):
        self.__estado = novo_estado
    @nome.setter
    def nome(self, novo_nome:str):
        if novo_nome is None:
         raise Exception("nome é obrigatorio")
        self.__nome = novo_nome.title().strip()
    @descricao.setter
    def descricao(self, nova_descricao:str):
        if len(nova_descricao.strip()) < 5:
             raise Exception("deve ser maior que 5 caracteteres")
        self.__descricao = nova_descricao.strip()
   
    @recompensa.setter
    def recompensa(self, nova_recompensa:str):
        if nova_recompensa < 1 or nova_recompensa > 100:
             raise Exception("deve ser entre 1 e 100")
        self.__recompensa = nova_recompensa
   
    def exibir_dados(self):
         return f"""
         ====== MISSÃO ======
         Nome: {self.nome}
         Descrição: {self.descricao}
         Recompensa: {self.recompensa}
         Estado: {type(self.__estado).__name__}"""
    
    def __str__(self):
        return self.exibir_dados()
    
    def __eq__(self, outra):
       return isinstance(outra, Missao) and self.nome == outra.nome
    
    def iniciar_missao(self):
        self.__estado.iniciar()
        
    def concluir_missao(self,valor):
        self.__estado.concluir(valor)