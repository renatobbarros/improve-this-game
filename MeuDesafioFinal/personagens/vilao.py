from .personagem import Personagem 
import random

class Vilao(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)

        if not self.habilidades:
            self.habilidades = {
                "Ataque Genérico": 10
            }

    def escolher_ataque_ia(self):
       
        if self.vida < self.vida_maxima * 0.4:
            if random.random() < 0.7:
                habilidade_mais_forte = max(self.habilidades, key=self.habilidades.get)
                return habilidade_mais_forte
        
        habilidade_escolhida = random.choice(list(self.habilidades.keys()))
        return habilidade_escolhida


    def __str__(self):
        return f'Vilão: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque_base}, Defesa: {self.defesa_base}'