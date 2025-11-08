from personagens.personagem import Personagem  
from .herois import Heroi

class Vilao(Personagem):
    def __init__(self, nome, idade, vida, maldade):
        super().__init__(nome, idade, vida)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade

    def ataque(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()

    def dialogar(self, outro):
        if isinstance(outro, Heroi):
            print(f"🗣️ {self.nome}: 'Tolo! Você acha que pode me derrotar, {outro.nome}?'")
        else:
            print(f"🗣️ {self.nome}: 'Saia do meu caminho, {outro.nome}.'")

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
