from Produto import Produto
from ProdutoAlimenticio import ProdutoAlimenticio

def menu():
    print("\n=== Controle de Estoque ===")
    print("1. Cadastrar Produto Comum")
    print("2. Cadastrar Produto Alimentício")
    print("3. Exibir Produtos Cadastrados")
    print("4. Repor Estoque")
    print("5. Vender Produto")
    print("0. Sair")

produtos = []

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        produto = Produto(nome, preco, quantidade)
        produtos.append(produto)
        print("Produto comum cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do produto alimentício: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        validade = input("Data de validade (dd/mm/aaaa): ")
        produto_alimenticio = ProdutoAlimenticio(nome, preco, quantidade, validade)
        produtos.append(produto_alimenticio)
        print("Produto alimentício cadastrado com sucesso!")

    elif opcao == "3":
        print("\n--- Produtos Cadastrados ---")
        for produto in produtos:
            produto.exibir_produtos()

    elif opcao == "4":
        nome = input("Nome do produto a repor: ")
        encontrado = False
        for produto in produtos:
            if produto.nome.lower() == nome.lower():
                qtd = int(input("Quantidade a adicionar: "))
                produto.repor_estoque(qtd)
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "5":
        nome = input("Nome do produto a vender: ")
        encontrado = False
        for produto in produtos:
            if produto.nome.lower() == nome.lower():
                qtd = int(input("Quantidade a vender: "))
                produto.vender(qtd)
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
