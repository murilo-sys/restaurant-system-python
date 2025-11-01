class Restaurante:

    def __init__(self, nome):
        self.nome = nome
        self.rendimento = 0.0
        self.clientes = 0

    def registrar_venda(self, preco_produto: float) -> tuple[bool, str]:
        if preco_produto > 0:
            self.rendimento += preco_produto
            self.clientes += 1
            return True, f"Prato registrado no valor de R${preco_produto}"
        return False, "Valor inválido, favor inserir um valor maior que 0"

    def resultados (self):
        print(f" Resultados ".center(25,"="), 
              f"\nVocê vendeu R${self.rendimento}"
              f"\nVocê atendeu {self.clientes} cliente(s)")
