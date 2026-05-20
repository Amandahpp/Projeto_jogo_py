from abc import ABC,abstractmethod

class EstadoMissao(ABC):
     def __init__(self,missao):
          self.missao = missao

     @abstractmethod
     def iniciar(self):
          pass
     @abstractmethod
     def concluir(self):
          pass
     
class EstadoPendente(EstadoMissao):
     def iniciar(self):
          print(f"A missao '{self.missao.nome}'começou")
          self.missao.estado = EstadoAndamento(self.missao)
     def concluir(self):
           print("A missão precisa ser iniciada antes.")

class EstadoAndamento(EstadoMissao):
       def iniciar(self):
           print("A missão ja esta em andamento.")

       def concluir(self,valor):
             if valor > 0:
                  print("missao concluida")
                  self.missao.estado = EstadoCompletada(self.missao)
                  print(f"Você ganhou {valor} XP!")
             else:
                   print("Missão fracassada!")
                   self.missao.estado = EstadoFracassada(self.missao)
                   
class EstadoCompletada(EstadoMissao):
     def iniciar(self):
        print("A missão já foi concluída.")

     def concluir(self):
        print("A missão já foi concluída.")

class EstadoFracassada(EstadoMissao):

    def iniciar(self):
        print("A missão fracassou.")

    def concluir(self):
        print("A missão fracassou.")

