class Restaurante:

    def __init__(self, nome):
        self.nome = nome
        self.rendimento = 0.0
        self.clientes = 0

    def registrarVenda(self, preco_produto: float) -> bool:
        if preco_produto > 0:
            self.rendimento += preco_produto
            return True
        else:
            return False
