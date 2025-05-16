class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_produtos(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Quantidade: {self.quantidade}")

    def repor_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque de '{self.nome}'.")

    def vender(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades de '{self.nome}' vendidas com sucesso.")
        else:
            print(f"Estoque insuficiente. Estoque atual: {self.quantidade}")
