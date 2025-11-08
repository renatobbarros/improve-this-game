from . import interface  
import random

def iniciar_batalha(heroi, vilao):
    
    turno = 1
    while heroi.esta_vivo() and vilao.esta_vivo():
        interface.limpar_tela()
        print(f"--- Turno {turno} ---")
        interface.exibir_hud_batalha(heroi, vilao)
        
        escolha = interface.exibir_menu_acoes(heroi)
        
        if escolha == '1':
            heroi.atacar(vilao)
        elif escolha == '2':
            heroi.usar_pocao()
        elif escolha == '3':
            heroi.usar_habilidade_especial(vilao)
        elif escolha == '4':
            heroi.dialogar(vilao)
        elif escolha == '0':
            print(f"{heroi.nome} fugiu da batalha!")
            break
        else:
            print("Ação inválida. Você perdeu o turno!")
            
        
        if not vilao.esta_vivo():
            break
            
        input("\nPressione ENTER para continuar...")
        
        interface.limpar_tela()
        print(f"--- Turno {turno} (Vez de {vilao.nome}) ---")
        interface.exibir_hud_batalha(heroi, vilao)
        
        # 70% de chance de atacar, 30% de dialogar.
        if random.randint(1, 10) <= 7:
            vilao.atacar(heroi)
        else:
            vilao.dialogar(heroi)
            
        
        if not heroi.esta_vivo():
            break

        input("\nPressione ENTER para continuar...")
        turno += 1


    interface.limpar_tela()
    if heroi.esta_vivo() and not vilao.esta_vivo():
        print("---------------------------")
        print(f"{heroi.nome} venceu a batalha.")
        print("---------------------------")
    elif not heroi.esta_vivo():
        print("---------------------------")
        print(f"{vilao.nome} venceu a batalha.")
        print("---------------------------")