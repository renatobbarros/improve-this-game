from utilidades.textos import limpar_tela, esperar_tecla


log_de_batalha = []

def registrar_acao(acao):

    print(acao) 
    log_de_batalha.append(acao)

def exibir_hud_batalha(jogador, vilao):
    print("=" * 30)
    try:
        vida_jogador_percent = (jogador.vida / jogador.vida_maxima)
    except ZeroDivisionError:
        vida_jogador_percent = 0
    barra_jogador = "█" * int(vida_jogador_percent * 20)
    print(f"{jogador.nome}: {jogador.vida}/{jogador.vida_maxima}")
    print(f"[{barra_jogador:<20}] {int(vida_jogador_percent * 100)}%")
    
    print("-" * 30)
    
    try:
        vida_vilao_percent = (vilao.vida / vilao.vida_maxima)
    except ZeroDivisionError:
        vida_vilao_percent = 0
    barra_vilao = "█" * int(vida_vilao_percent * 20)
    print(f"{vilao.nome}: {vilao.vida}/{vilao.vida_maxima}")
    print(f"[{barra_vilao:<20}] {int(vida_vilao_percent * 100)}%")
    print("=" * 30)

def iniciar_batalha(jogador, vilao):

    limpar_tela()
    print(f"A BATALHA VAI COMEÇAR! {jogador.nome} VS {vilao.nome}")
    esperar_tecla()

    while jogador.esta_vivo() and vilao.esta_vivo():
        limpar_tela()
        exibir_hud_batalha(jogador, vilao)
        
        print(f"\n--- Turno de {jogador.nome} ---")
        print("O que você vai fazer?")
        print("  1. Atacar (Estudar)")
        print("  2. Usar Livro (Mochila)")
        print("  3. Ver Status Próprio")

        escolha_turno = ""
        while escolha_turno not in ["1", "2", "3"]:
            escolha_turno = input("Digite sua escolha (1, 2 ou 3): ")

        if escolha_turno == "1":
            habilidade = jogador.escolher_acao_ataque()
            dano = jogador.atacar(vilao, habilidade)
            registrar_acao(f"[Batalha] {jogador.nome} usou '{habilidade}' e causou {dano} de dano.")

        elif escolha_turno == "2":
            livro = jogador.escolher_acao_inventario()
            if livro:
                jogador.usar_livro(livro)
                registrar_acao(f"[Batalha] {jogador.nome} usou o item '{livro}'.")
            else:
                registrar_acao(f"[Batalha] {jogador.nome} ficou indeciso e perdeu o turno.")
                
        elif escolha_turno == "3":
            jogador.mostrar_status()
            esperar_tecla()
            continue

        if not vilao.esta_vivo():
            print(f"{vilao.nome} foi derrotado!")
            return True 

        esperar_tecla()

        limpar_tela()
        exibir_hud_batalha(jogador, vilao)
        print(f"\n--- Turno de {vilao.nome} ---")
        
        habilidade_vilao = vilao.escolher_ataque_ia()
        dano_vilao = vilao.atacar(jogador, habilidade_vilao)
        registrar_acao(f"[Batalha] {vilao.nome} usou '{habilidade_vilao}' e causou {dano_vilao} de dano.")

        if not jogador.esta_vivo():
            print(f"{jogador.nome} foi reprovado... Que pena.")
            return False 
            
        esperar_tecla()

    return jogador.esta_vivo()

def exibir_log_final():
    limpar_tela()
    print("--- Histórico de Eventos (Log de Ações) ---")
    for acao in log_de_batalha:
        print(f"- {acao}")