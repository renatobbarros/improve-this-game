import time
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from personagens.heroi import Heroi
from personagens.vilao import Vilao
from personagens.personagem import Personagem
from utilidades.logica import iniciar_batalha, exibir_log_final
from utilidades.textos import limpar_tela, esperar_tecla, exibir_narracao, exibir_dialogo

def iniciar_jogo():
    limpar_tela()
    
    exibir_narracao("Você, um calouro cheio de sonhos (e sono), chega na lendária...")
    time.sleep(1)
    exibir_narracao("U.F.C.E.C. - Universidade Federal de Coisas Extremamente desnecessariamente Complicadas")
    
    nome_jogador = input("\nQual o seu nome, calouro(a)? ")
    if not nome_jogador:
        nome_jogador = "Estudante Anônimo"

    jogador = Heroi(nome=nome_jogador, vida=100, ataque=15, defesa=10)
    
    exibir_narracao("Você é recepcionado por duas figuras imponentes...")
    
    reitor_neymar = Personagem("Reitor Neymar", 999, 999, 999)
    maldanado = Vilao("Prof. Maldanado", 80, 20, 10)
    
    maldanado.habilidades = {
        "Casca de Banana": 15,
        "Por que você está aqui?": 20
    }
    
    time.sleep(1)
    exibir_dialogo(reitor_neymar.nome, f"Seja bem-vindo(a), {jogador.nome}! Aproveite sua... 'aventura'. Tenho que ir, tchau!")
    exibir_dialogo(maldanado.nome, "Olá, estudante. Serei seu professor de 'Calculo 1'.")
    exibir_narracao("O Reitor Neymar sai, e Maldanado revela seu lado mal.")
    time.sleep(1)
    
    exibir_dialogo(maldanado.nome, "Heh... 'aventura'. Você não sabe onde se meteu, calouro(a).")
    exibir_dialogo(maldanado.nome, "Acha que só porque 'gosta de computador' vai se dar bem? Aqui o buraco é mais embaixo!")
    exibir_narracao("Maldanado te assusta... é hora da primeira prova!")
    
    esperar_tecla("Pressione Enter para iniciar a Prova 1 (Batalha)...")

    vitoria_ato_1 = iniciar_batalha(jogador, maldanado)

    if not vitoria_ato_1:
        limpar_tela()
        exibir_narracao("Você não conseguiu... Maldanado te reprovou.")
        exibir_dialogo(maldanado.nome, "Eu avisei. Talvez SI não seja para você.")
        exibir_narracao("REPROVADO. Fim de Jogo.")
        return 


    limpar_tela()
    exibir_narracao("Você entrega a prova. Maldanado te olha com surpresa.")
    exibir_dialogo(maldanado.nome, "Você... passou? IMPOSSÍVEL! Mas tudo bem, pode ir. Por enquanto.")
    exibir_narracao("Maldanado desiste de te importunar.")
    
    jogador.ganhar_xp(50)
    jogador.inventario["Livro de Cálculo (Cura)"] = jogador.inventario.get("Livro de Cálculo (Cura)", 0) + 1
    
    exibir_narracao("Você ganhou 50 XP pela vitória e achou um 'Livro de Cálculo (Cura)'!")
    jogador.curar(30) 
    
    esperar_tecla("Pressione Enter para ir para o Ato 2...")

    limpar_tela()
    exibir_narracao("Você se recupera e vai para a próxima aula, mas um veterano bloqueia a porta.")
    
    vermelindo = Vilao("Vermelindo (Veterano)", 120, 25, 15)
    vermelindo.habilidades = {
        "Por que você está aqui?": 20,
        "Questão Difícil": 30,
        "Isso é Coisa de Calouro": 25
    }

    exibir_dialogo(vermelindo.nome, "Opa, opa, calouro(a). Acha que é só chegar e entrar?")
    exibir_dialogo(vermelindo.nome, "Aqui na UFCEC, primeiro período não tem vez. Para ganhar meu respeito, vai ter que provar que merece.")
    
    esperar_tecla("Pressione Enter para iniciar o Debate (Batalha)...")

    vitoria_ato_2 = iniciar_batalha(jogador, vermelindo)

    if not vitoria_ato_2:
        limpar_tela()
        exibir_narracao("Vermelindo te humilhou na frente da turma.")
        exibir_dialogo(vermelindo.nome, "Fraco. Volte semestre que vem.")
        exibir_narracao("REPROVADO. Fim de Jogo.")
        return 

    limpar_tela()
    exibir_narracao("Você derrotou Vermelindo! Ele está chocado.")
    exibir_dialogo(vermelindo.nome, "Caramba... Você sabe do que está falando. Foi mal.")
    exibir_dialogo(vermelindo.nome, f"Pode entrar, {jogador.nome}. Quer dizer... colega. Senta aí.")
    
    exibir_narracao("VOCÊ VENCEU! 🏆")
    exibir_narracao(f"Parabéns, {jogador.nome}! Você sobreviveu ao primeiro período na UFCEC.")
    exibir_narracao(f"XP Final: {jogador.xp}")
    
    esperar_tecla()
    
    exibir_log_final()
    exibir_narracao("\n--- FIM ---")


if __name__ == "__main__":
    iniciar_jogo()
