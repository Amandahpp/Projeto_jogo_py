
from personagens import Personagens
from missaocombate import MissaoCombate
from missaocoleta import MissaoColeta
from missaopexploracao import MissaoExploracao

personagem_teste = Personagens("Joao",15)
print(personagem_teste.exibir_dados())

m1 = MissaoCombate(
    "Guerra Orc",
    "Derrotar orcs",
    100,
    "Orc",
    10
)
m1.iniciar_missao()

m1.concluir_missao(10)

print(m1.exibir_dados())

m2 = MissaoColeta(
    "Coleta de Madeira",
    "Coletar recursos",
    50,
    "Madeira",
    20
)

m2.iniciar_missao()

m2.concluir_missao(20)

print(m2.exibir_dados())


m3 = MissaoExploracao(
    "Explorar Floresta",
    "Descobrir região",
    80,
    "Floresta Negra",
    15.5
)

m3.iniciar_missao()

m3.concluir_missao(15.5)

print(m3.exibir_dados())


personagem_teste.adicionar_missao(m1)
personagem_teste.adicionar_missao(m2)

print("Missões do personagem:")

personagem_teste.listar_missoes()

