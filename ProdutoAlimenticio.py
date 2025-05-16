from Produto import Produto

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco, quantidade, data_validade):
        super().__init__(nome, preco, quantidade)
        self.data_validade = data_validade

    def exibir_produtos(self):
        print(f"Produto Alimentício: {self.nome} | Preço: R${self.preco:.2f} | Quantidade: {self.quantidade} | Validade: {self.data_validade}")
