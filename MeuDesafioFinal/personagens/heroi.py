from .personagem import Personagem 

class Heroi(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        
        self.xp = 0
        

        self.habilidades = {
            "Prestei Atenção": 20,
            "Respondi Listas": 25,
            "Dominei o Conteúdo": 35
        }
        
        self.inventario = {
            "Livro de Cálculo (Cura)": 2,
            "Livro de Lógica (Ataque)": 1
        }

    def usar_livro(self, nome_livro):
        if nome_livro not in self.inventario or self.inventario[nome_livro] == 0:
            print(f"Você não tem '{nome_livro}' na mochila.")
            return False

        self.inventario[nome_livro] -= 1
        print(f"Você usou 1 '{nome_livro}'. Restantes: {self.inventario[nome_livro]}")

        if "Cura" in nome_livro:
            pontos_cura = 30
            self.curar(pontos_cura)
            print(f"Você revisou a matéria e se sente melhor. (+{pontos_cura} Vida)")
            
        elif "Ataque" in nome_livro:
            boost_ataque = 5
            self.ataque_base += boost_ataque
            print(f"Você se sente mais confiante! (+{boost_ataque} Ataque Base)")

        self.ganhar_xp(10)
        return True

    def ganhar_xp(self, pontos):
        self.xp += pontos
        print(f"🧠 {self.nome} ganhou {pontos} XP! (Total: {self.xp} XP)")

    def escolher_acao_ataque(self):
        print("Escolha sua habilidade de ataque (Estudo):")
        habilidades_lista = list(self.habilidades.keys())
        for i, nome in enumerate(habilidades_lista):
            dano = self.habilidades[nome]
            print(f"  {i+1}. {nome} (Dano: {dano})")
        
        while True:
            try:
                escolha = int(input("Digite o número da habilidade: ")) - 1
                if 0 <= escolha < len(habilidades_lista):
                    return habilidades_lista[escolha]
                else:
                    print("Escolha inválida.")
            except ValueError:
                print("Por favor, digite um número.")

    def escolher_acao_inventario(self):
        print("Escolha um livro para usar (Mochila):")
        inventario_lista = [livro for livro, qtd in self.inventario.items() if qtd > 0]
        
        if not inventario_lista:
            print("Sua mochila está vazia.")
            return None

        for i, nome in enumerate(inventario_lista):
            print(f"  {i+1}. {nome} (Qtd: {self.inventario[nome]})")
        
        print(f"  {len(inventario_lista) + 1}. Voltar")

        while True:
            try:
                escolha = int(input("Digite o número do item: ")) - 1
                if 0 <= escolha < len(inventario_lista):
                    return inventario_lista[escolha]
                elif escolha == len(inventario_lista): 
                    return None
                else:
                    print("Escolha inválida.")
            except ValueError:
                print("Por favor, digite um número.")