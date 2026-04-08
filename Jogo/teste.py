from missao import Missao
from personagens import Personagens
from missaocombate import MissaoCombate
from missaocoleta import MissaoColeta
from missaopexploracao import MissaoExploracao

personagem_teste = Personagens("Joao")
print(personagem_teste.exibir_dados())

personagem_teste2 = Personagens(nome="Maria")
print(personagem_teste2.exibir_dados())
print(personagem_teste2)

personagem_teste.ganha_xp(50)
personagem_teste.perde_vida(10)
personagem_teste.aumenta_nivel()

print(personagem_teste.exibir_dados())

missao_teste = Missao("Derrotar Dragao", "Derrote o chefe final", 99)
missao_teste.exibir_dados()


###### testes missao 

# Criando objetos

m1 = MissaoCombate("Guerra Orc", "Derrotar orcs", 100, "Orc", 10)
m1.exibir_dados()
m1.iniciar_missao()
m1.exibir_dados()
m1.concluir_missao()
m1.exibir_dados()
m2 = MissaoColeta("Coleta de Madeira", "Coletar recursos", 50, "Madeira", 20)

m2.iniciar_missao()
m2.concluir_missao()
m2.exibir_dados()
m3 = MissaoExploracao("Explorar Floresta", "Descobrir região", 80, "Floresta Negra", 15.5)

m3.iniciar_missao()
m3.concluir_missao()
m3.exibir_dados()




