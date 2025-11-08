import time
import sys
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla(mensagem="[Pressione Enter para continuar...]"):
    print(f"\n{mensagem}\n")
    input()

def exibir_narracao(texto, delay=0.03):
    print("---")
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n---")

def exibir_dialogo(personagem_nome, texto, delay=0.03):
    dialogo_formatado = f"💬 {personagem_nome}: "
    print(dialogo_formatado, end='')
    
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()