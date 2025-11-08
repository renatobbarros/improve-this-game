from personagens.herois import Heroi
from personagens.vilao import Vilao
from utilidades.logica import iniciar_batalha
import random

status_herois = [
    {"nome": "Aragorn", "vida": 120, "ataque": 18, "defesa": 10, "habilidade": "Golpe Real"},
    {"nome": "Gandalf", "vida": 80, "ataque": 25, "defesa": 5, "habilidade": "Bola de Fogo"},
]

status_viloes = [
    {"nome": "Dragão Smaug", "vida": 200, "ataque": 22, "defesa": 12},
    {"nome": "Ork Lurtz", "vida": 90, "ataque": 15, "defesa": 8},
]

# Usando listas para armazenar os objetos.
lista_de_herois = []
for status in status_herois:
    lista_de_herois.append(
        Heroi(status["nome"], status["vida"], status["ataque"], status["defesa"], status["habilidade"])
    )

lista_de_viloes = []
for status in status_viloes:
    lista_de_viloes.append(
        Vilao(status["nome"], status["vida"], status["ataque"], status["defesa"])
    )


print("Bem-vindo ao jogo do desafio.")
print("Escolha seu Herói:")
for i, heroi in enumerate(lista_de_herois):
    print(f"{i+1}. {heroi.nome}")

escolha_heroi = int(input("> ")) - 1
jogador = lista_de_herois[escolha_heroi]

inimigo = random.choice(lista_de_viloes)

print(f"\nUm {inimigo.nome} selvagem aparece!\n")
input("Pressione ENTER para iniciar a batalha...")

# Chama a função que contém o loop da batalha
iniciar_batalha(jogador, inimigo)

print("\n--- Fim de Jogo ---")