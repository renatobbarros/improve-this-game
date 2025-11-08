import random

class Personagem:

    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida
        self.ataque_base = ataque
        self.defesa_base = defesa
        

        self.inventario = {}  

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo, nome_habilidade):
        if not self.esta_vivo():
            return

        if nome_habilidade not in self.habilidades:
            print(f"{self.nome} tentou usar '{nome_habilidade}' mas falhou.")
            return 0
            
        dano_habilidade = self.habilidades[nome_habilidade]
        
        dano_bruto = self.ataque_base + dano_habilidade
        dano_liquido = dano_bruto - alvo.defesa_base
        
        if dano_liquido < 0:
            dano_liquido = 0
        
        dano_final = round(dano_liquido * random.uniform(0.9, 1.1))

        print(f"💥 {self.nome} usou '{nome_habilidade}' contra {alvo.nome}!")
        alvo.receber_dano(dano_final)
        return dano_final

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"🩸 {self.nome} recebeu {dano} de dano! Vida restante: {self.vida}/{self.vida_maxima}")

    def curar(self, pontos_cura):
        self.vida += pontos_cura
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
        print(f"✨ {self.nome} se curou! Vida atual: {self.vida}/{self.vida_maxima}")

    def dialogar(self, mensagem):
        print(f"💬 {self.nome}: \"{mensagem}\"")

    def mostrar_status(self):
        print(f"--- STATUS: {self.nome} ---")
        print(f"  Vida: {self.vida} / {self.vida_maxima}")
        print(f"  Ataque: {self.ataque_base}")
        print(f"  Defesa: {self.defesa_base}")
        print(f"  Habilidades: {', '.join(self.habilidades.keys())}")
        print(f"  Inventário: {self.inventario}")
        print("-------------------------")