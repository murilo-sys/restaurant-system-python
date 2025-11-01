class Restaurante:

    def __init__(self, nome):
        self.nome = nome
        self.rendimento = 0.0
        self.clientes = 0

    def registrarVenda(self, preco_produto: float) -> bool:
        if preco_produto > 0:
            self.rendimento += preco_produto
            print(f"Prato registrado no valor de R${preco_produto}")
            return True
        else:
            print("Valor inválido, favor inserir um valor maior que 0")
            return False
