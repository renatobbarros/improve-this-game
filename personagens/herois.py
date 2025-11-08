from .personagem import Personagem
from .vilao import Vilao

class Heroi(Personagem):
    
    def __init__(self, nome, vida, ataque, defesa, habilidade_especial):
        super().__init__(nome, vida, ataque, defesa)
        # Define que a habilidade especial tem um atributo especifico.
        self.habilidade_especial = habilidade_especial
        self.pocoes = 3 

    # 3. Adiciona métodos específicos do Heroi
    def usar_pocao(self):
        if self.pocoes > 0:
            self.vida += 20  # Cura 20 de HP
            self.pocoes -= 1
            print(f"✨ {self.nome} usou uma poção e recuperou 20 de vida! (Poções restantes: {self.pocoes})")
        else:
            print(f"🚫 {self.nome} não tem mais poções!")

    def usar_habilidade_especial(self, alvo):
        # 'alvo' deve ser um objeto (neste caso, um Vilao)
        dano_especial = self.ataque * 2 # Exemplo: dano dobrado
        print(f"💥 {self.nome} usa '{self.habilidade_especial}' em {alvo.nome}!")
        alvo.receber_dano(dano_especial)

    def dialogar(self, outro):
        if isinstance(outro, Vilao):
            print(f"🗣️ {self.nome}: 'Agora, e a hora da verdade, {outro.nome}.'")
        else:
            print(f"🗣️ {self.nome}: 'Olá, {outro.nome}.'")