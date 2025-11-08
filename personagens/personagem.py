class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa
        
        # Garante que o dano seja pelo menos 1 (para não curar o inimigo).
        if dano < 1:
            dano = 1
            
        print(f"⚔️ {self.nome} ataca {alvo.nome} e causa {dano} de dano!")
        alvo.receber_dano(dano)

    def receber_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida < 0:
            self.vida = 0 

    def esta_vivo(self):
        return self.vida > 0

    def exibir_status(self):
        print(f"[{self.nome}] HP: {self.vida} | ATK: {self.ataque} | DEF: {self.defesa}")