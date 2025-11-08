import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_hud_batalha(heroi, vilao):
    print("=" * 30)
    print(f"🟢 {heroi.nome: <15} | HP: {heroi.vida:<5}")
    print(f"🔴 {vilao.nome: <15} | HP: {vilao.vida:<5}")
    print("=" * 30)

def exibir_menu_acoes(heroi):
    print("\nEscolha sua ação:")
    print("1. Atacar")
    print(f"2. Usar Poção ({heroi.pocoes} restantes)")
    print("3. Usar Habilidade Especial")
    print("4. Dialogar com o inimigo")
    print("0. Fugir")
    return input("Sua escolha: ")