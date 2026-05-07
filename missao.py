from status import Status

class Missao:
    def __init__(self,nome:str, descricao:str, recompensa:int):
        self.__nome = ""       
        self.__descricao = ""
        self.__recompensa = 0

        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.__status = Status.PENDENTE
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
    def status(self):
        return self.__status
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
   
    
    @status.setter
    def status(self, novo_status:str):
        novo_status = novo_status.upper().strip()
        if novo_status == "EM ANDAMENTO" and self.__status == "PENDENTE":
            self.__status = novo_status
        elif novo_status == "CONCLUIDA" and self.__status == "EM ANDAMENTO":
            self.__status = novo_status
        else:
            raise ValueError("Transição inválida")
    def exibir_dados(self):
        print( f"Nome: {self.nome}- Descrição: {self.descricao}- Recompensa {self.recompensa}- Status { self.__status.name}")
    
    def __str__(self):
        return self.exibir_dados()
    
    def __eq__(self, outra):
       return isinstance(outra, Missao) and self.nome == outra.nome
    
    def iniciar_missao(self):
      if self.__status == Status.PENDENTE:
        self.__status = Status.EM_ANDAMENTO
        print(f"A missão '{self.__nome}' começou! Objetivo: {self.__descricao}")
      else:
        print("Erro: A missão não pode ser iniciada novamente.")

    def concluir_missao(self):
      if self.__status == Status.EM_ANDAMENTO:
        self.__status = Status.CONCLUIDA
        print(f"Missão concluída com sucesso! Recompensa de {self.__recompensa} XP disponível.")
      else:
        print("Erro: A missão não pode ser concluída neste estado.")    